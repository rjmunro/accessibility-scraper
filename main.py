import json
import urllib2
from pprint import pprint

def getHeaders(pageObj):
    return {
        'poweredBy': pageObj.info().getheader('X-powered-by'),
        'server': pageObj.info().getheader('Server')
    }

siteFile = open('all-sites.json');
#siteFile = open('test-data.json');
sites = json.load(siteFile)
for site in sites:
    homePageObj = urllib2.urlopen(site['site-url'])

    site['headers'] = getHeaders(homePageObj)

    # Print site on screen. TODO: Save this info to a file
    pprint(site)

siteFile.close()


