#!/usr/bin/env python
import io
import re
import json
import urllib2
import lxml.html
from doctype import getDoctype
from pprint import pprint
import lxml.html
import codecs

nameRegexs = [
    re.compile(r"www\.([^.]*)\."),
    re.compile(r"http://(.*)\.nhs.uk"),
    re.compile(r"http://([^.]*)\.")
]

swfpat = re.compile("\.swf$")

class NoRedirection(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()

        return response

    https_response = http_response

opener = urllib2.build_opener(NoRedirection)

def getHeaders(pageObj):
    return {
        'poweredBy': pageObj.info().getheader('X-powered-by'),
        'server': pageObj.info().getheader('Server')
    }

def checkFile(url):
    fileBool = False
    fileText = ""
    try:
        fileCall = opener.open(url)
        if (fileCall.getcode() != 200):
            # we've been redirected
            fileBool = False
        else:
            fileBool = True
        fileText = fileCall.read()
    except urllib2.HTTPError, e:
        fileBool = False
    except urllib2.URLError, e:
        fileBool = False
    return {'present': fileBool, 'contents' : fileText}

def checkLinkTags(pageHtml):
    linkTags = pageHtml.cssselect('link')
    links = {}
    for link in linkTags:
       links.setdefault(link.attrib['rel'].decode(),[]).append(link.attrib['href'].decode())
    return links

def checkSiteMap(robots, links):
    siteMapBool = False
    if 'sitemap' in links:
        siteMapBool = True
    else:
        try:
            robotsText = robots
            siteMapBool = 'Sitemap' in robotsText
        except urllib2.HTTPError, e:
            siteMapBool = False
    return siteMapBool

def getSsl(site, homePageObj):
    if site['site-url'].startswith("https:"):
        return "always"

    if homePageObj.url.startswith("https:"):
        # We've been redirected
        return "always"

    return checkFile('https' + site['site-url'][4:])['present'] and "yes" or "no"

def getCMS(homepageText, robotsText):
    if 'Joomla' in robotsText:
        return 'Joomla'

    return 'Unknown'

def concatScripts(baseurl, root):
    #gather up all the scripts
    jsscripts = root.findall(".//script[@type='text/javascript']")
    allscripts = ''
    for script in jsscripts:
        if 'src' in script.attrib:
            #TODO: check for absolute URLs
            scriptgot = checkFile(baseurl + script.attrib['src'])
            if scriptgot['present']:
                allscripts = allscripts + "\n" + scriptgot['contents']
        else:
            allscripts = allscripts+"\n"+script.text
    return allscripts

def checkFlash(document, script):
    for e in document.findall(".//embed"):
        if 'src' in e.attrib['src'] and swfpat.search(e.attrib['src']):
            return True
    return "swflash.cab" in script

#siteFile = open('all-sites.json');
siteFile = open('test-data.json');
sites = json.load(siteFile)
for site in sites:
    homePageObj = urllib2.urlopen(site['site-url'])
    robots = checkFile(site['site-url'] + '/robots.txt')
    humans = checkFile(site['site-url'] + '/humans.txt')
    homePageHtml = homePageObj.read()
    if homePageHtml.startswith(codecs.BOM_UTF8):
        homePageHtml = homePageHtml[len(codecs.BOM_UTF8):]
    rootNode = lxml.html.fromstring(homePageHtml)
    site['doctype'] = getDoctype(homePageHtml)
    links = checkLinkTags(rootNode)

    scriptraw = concatScripts(site['site-url'], rootNode)

    site['headers'] = getHeaders(homePageObj)
    site['robots'] = robots['present']
    site['sitemap'] = checkSiteMap(robots['contents'], links)
    site['humans'] = humans['present']
    site['ssl'] = getSsl(site, homePageObj)
    site['cms'] = getCMS(homePageHtml, robots['contents'])
    site['changesEachLoad'] = checkFile(site['site-url'])['contents'] != homePageHtml
    site['flash'] = checkFlash(rootNode,scriptraw)

    for re in nameRegexs:
        m = re.search(site['site-url'])
        if m:
           cleanname = m.groups(1)[0]
           break

    with io.open('output/%s.json' % cleanname, 'wb') as outfile:
        json.dump(site, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        outfile.write("\n")

    if robots['present']:
        with io.open('output/%s-robots.txt' % cleanname, 'wb') as outfile:
            outfile.write(robots['contents']);

    print "Done '%s' in file '%s.json'" % (site['name'], cleanname)

siteFile.close()


