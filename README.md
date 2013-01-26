accessibilty-scraper
====================

Scripts to scrape a site and detect information about the accessibility and other technology it's using.

We aim to detect as many of the following features as possible:

Done
----
[nothing yet]

TODO:
-----

Useful files on site:
* robots.txt
* XML site map
* humans.txt
* Favicon, apple touch icon etc. - (might check for standard ones from wordpress etc)

Server:
* Server tech (from headers)
* Hosting company (from whois of IP address)
* https avaialable
* https by default (are we redirected)

HTML:
* doctype
* HTML tags & attributes in use (HTML5 etc.)
* Alt tags on images
* Screen reader hints (aria attributes)
* Use of Flash
* Look for CMS signatures Wordpress etc.
* CDN for images
* IE Conditional comments
* JS use / jQuery etc.
* Use of Google translate
* Welsh & other language content
* Initial redirect?
* HTML validitiy
* RSS Links
* Tables for layout?

Multiple passes:
* Anything randomized each hit
* Different site if you send mobile user agent

CSS:
* css selectors that are used
* Media query use, other CSS use
* Font sizes
* Browser detection hacks being used
* CSS valid
* CSS minified

Whole content:
* Size of download for initial view (download time)

Other (whole site scanning?):
* Friendly URLs
  - could scan sitemap if available
* PDFs to download, word docs to download
* Any AJAX use?

