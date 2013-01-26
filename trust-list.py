import lxml.html 
import urllib2


trustList = urllib2.urlopen('http://www.nhs.uk/ServiceDirectories/Pages/AcuteTrustListing.aspx')
html = trustList.read()
     
root = lxml.html.fromstring(html)
for tr in root.cssselect(".trust-list li a"):
	href = tr.attrib['href'].decode()

	innerhtmlCall = urllib2.urlopen("http://www.nhs.uk/" + href)
	innerhtml = innerhtmlCall.read()
	inneroot = lxml.html.fromstring(innerhtml)
	web = inneroot.cssselect(".panel-profile-site .panel-content .pad p a")
	try:
		website = web[0].attrib['href'].decode()
	except:
		website = "parser issue :("
	try:
		title = tr.attrib['title'].decode()
	except:
		title = 'parser issue :('
	if(href.startswith('/Services/')):
		data = {
			'url' : 'http://nhs.uk' + href,
			'name': title.replace('View details for ',''),
			'trust-url': website
		}

