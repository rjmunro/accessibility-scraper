import json
import os
import io

def custom_listdir(path):
    dirs = sorted([d for d in os.listdir(path) if os.path.isdir(path + os.path.sep + d)])
    dirs.extend(sorted([f for f in os.listdir(path) if os.path.isfile(path + os.path.sep + f)]))
    dirs = [x for x in dirs if not x.startswith('.')]
    return dirs

path = 'output/'
listing = custom_listdir(path)
listingLength = len(listing)

#counting variables
robotsTrue = 0
robotsFalse = 0
humansTrue = 0
doctypes = {}
servers = {}
frameworks = {}
sitemapTrue = 0
sslTrue = 0

#the loop
for infile in listing:
    jsonFile = open(path + infile)
    siteJSON = json.load(jsonFile)
    if siteJSON['robots'] == True:
        robotsTrue+=1
    else:
        robotsFalse+=1
    if siteJSON['humans'] == True:
        humansTrue+=1
    doctypes[siteJSON['doctype']] = doctypes.setdefault(siteJSON['doctype'],0) + 1
    servers[siteJSON['headers']['server']] = servers.setdefault(siteJSON['headers']['server'],0) + 1
    frameworks[siteJSON['headers']['poweredBy']] = frameworks.setdefault(siteJSON['headers']['poweredBy'],0) + 1
    if siteJSON['sitemap'] == True:
        sitemapTrue+=1
    if siteJSON['ssl'] == 'yes':
        sslTrue+=1
#create JSONfile
overJSON = {'robotsTrue':robotsTrue,'robotsFalse':robotsFalse,'humansTrue':humansTrue,'doctypes':doctypes,'servers':servers,'frameworks':frameworks,'sitemap':sitemapTrue,'ssl':sslTrue}
#print
outfile = io.open('output/overview.json', 'wb')
json.dump(overJSON, outfile, sort_keys = True, indent=4, separators=(',', ': '))
outfile.write('\n')
