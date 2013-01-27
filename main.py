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

def getHeaders(pageObj):
    return {
        'poweredBy': pageObj.info().getheader('X-powered-by'),
        'server': pageObj.info().getheader('Server')
    }

def checkFile(url):
    fileBool = False
    fileText = ""
    try:
        fileCall = urllib2.urlopen(url)
        fileText = fileCall.read()
        fileBool = True
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

    return checkFile('https' + site['site-url'][4:]) and "yes" or "no"


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

    site['headers'] = getHeaders(homePageObj)
    site['robots'] = robots['present']
    site['sitemap'] = checkSiteMap(robots['contents'], links)
    site['humans'] = humans['present']
    site['ssl'] = getSsl(site, homePageObj)

    for re in nameRegexs:
        m = re.search(site['site-url'])
        if m:
           cleanname = m.groups(1)[0]
           break

    with io.open('output/%s.json' % cleanname, 'wb') as outfile:
        json.dump(site, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        outfile.write("\n")

    print "Done '%s' in file '%s.json'" % (site['name'], cleanname)

siteFile.close()


