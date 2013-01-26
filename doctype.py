#!/usr/bin/env python
import re

doctypes = {
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 TRANSITIONAL//EN" "HTTP://WWW.W3.ORG/TR/1999/REC-HTML401-19991224/LOOSE.DTD">': 'HTML 4 (loose)',
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "HTTP://WWW.W3.ORG/TR/HTML4/STRICT.DTD">': 'HTML 4 (strict)',
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 TRANSITIONAL//EN" "HTTP://WWW.W3.ORG/TR/XHTML1/DTD/XHTML1-TRANSITIONAL.DTD">': 'XHTML 1.0 (loose)',
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 STRICT//EN" "HTTP://WWW.W3.ORG/TR/XHTML1/DTD/XHTML1-STRICT.DTD">': 'XHTML 1.0 (strict)',
    '<!DOCTYPE HTML>': 'HTML 5',
}

def getDoctype(homePageTxt):
    firstTag = homePageTxt.split(">")[0].strip() + ">"
    # Normalise spaces etc.
    firstTag = " ".join(firstTag.split())
    if firstTag.upper() in doctypes:
        return doctypes[firstTag.upper()]
    else:
        print "'"+firstTag.upper()+"': 'unknown',"
    if firstTag.startswith("<!DOC"):
        return firstTag


if __name__ == "__main__":
    print getDoctype("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">""")
