import json
import urllib2
from pprint import pprint

def getHeaders(pageObj):
    return {
        'poweredBy': pageObj.info().getheader('X-powered-by'),
        'server': pageObj.info().getheader('Server')
    }

def checkFile(url):
    fileBool = False
    try:
        fileCall = urllib2.urlopen(url)
        fileBool = True
    except urllib2.HTTPError, e:
        fileBool = False
    except urllib2.URLError, e:
        fileBool = False
    return fileBool

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

    site['headers'] = getHeaders(homePageObj)
    site['robots'] = checkFile(site['site-url'] + '/robots.txt')
    site['humans'] = checkFile(site['site-url'] + '/humans.txt')
    site['ssl'] = getSsl(site, homePageObj)

    # Print site on screen. TODO: Save this info to a file
    pprint(site)

siteFile.close()


