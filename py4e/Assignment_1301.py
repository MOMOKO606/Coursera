# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:47:58 2018

@author: bianl
"""

#  Assignment 13.1 Extracting Data from XML
#  From Course 3: Using Python to Access Web Data, Week 5(Chapter 13)
#  IMPORTANT knowledge points:
#  1. url & xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Input url
url = input('Enter -')
if len(url) < 1:url = 'http://py4e-data.dr-chuck.net/comments_87066.xml'
print('Retrieving', url)

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
print('Retrieved', len(data), 'characters')

counts = tree.findall('.//count')
total = 0.0
for i in range(len(counts)):
    x = counts[i].text
    total = total + float(x)

print(len(counts),total)

