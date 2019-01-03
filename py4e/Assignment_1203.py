# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:25:44 2018

@author: bianl
"""

#  Assignment 12.3 Following Links in HTML Using BeautifulSoup
#  From Course 3: Using Python to Access Web Data, Week 4(Chapter 12)
#  IMPORTANT knowledge points:
#  1. urllib, ssl, BeautifulSoup
#  2. regular expression

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input parameters & its default value
url = input('Enter - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Fyfe.html'    
pos = input('Enter position:')
if len(pos) < 1: pos = 18
loop = input('Enter count:')
if len(loop) < 1: loop = 7

for i in range(loop):
    print('Retrieving:',url)
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    urls = []
    for tag in tags:
        urls.append(tag.get('href', None))
    url = urls[pos-1]
    
print(re.findall('known_by_([A-Z]+[a-z]+)',url))
