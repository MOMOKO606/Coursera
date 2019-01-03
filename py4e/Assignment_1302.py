# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:04:05 2018

@author: bianl
"""

#  Assignment 13.2 Extracting Data from JSON
#  From Course 3: Using Python to Access Web Data, Week 6(Chapter 13)
#  IMPORTANT knowledge points:
#  1. url & json
#  2. encode & decode
#  3.json.dumps

import urllib.request, urllib.parse, urllib.error
import json

# Input url
url = input('Enter -')
if len(url) < 1: url = ' http://py4e-data.dr-chuck.net/comments_87067.json'
print('Retrieving', url)    
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
print(json.dumps(js,indent=4))

total = 0.0
for i in range(len(js['comments'])):
    total = total + js['comments'][i]['count']
print(total)       