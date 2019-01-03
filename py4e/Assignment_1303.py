# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:00:54 2018

@author: bianl
"""

#  Assignment 13.3 Using the GeoJSON API
#  From Course 3: Using Python to Access Web Data, Week 6(Chapter 13)
#  IMPORTANT knowledge points:
#  1. url & json
#  2. encode & decode
#  3.json.dumps

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
if len(address) < 1: address = "Monash University"

url = serviceurl + urllib.parse.urlencode({'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(json.dumps(js, indent=4))
print(js["results"][0]["place_id"])
    
