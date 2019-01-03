# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:10:00 2018

@author: bianl
"""

#  Assignment 12.2 Scraping HTML Data with BeautifulSoup
#  From Course 3: Using Python to Access Web Data, Week 4(Chapter 12)
#  IMPORTANT knowledge points:
#  1. urllib, ssl, BeautifulSoup
#  2. urlopen

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#  Set default url value
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_87064.html'
# Attention! different from Python2
html = urllib.request.urlopen(url, context=ctx).read()  

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0.0
# Attention! different from BeautifulSoup 3
tags = soup.find_all('span')  
for tag in tags:
    # Look at the parts of a tag
    value = tag.contents[0]
    print('TAG:', tag)
    print('Contents:', value)
    print('Attrs:', tag.attrs)
    count = count + float(value)
    
