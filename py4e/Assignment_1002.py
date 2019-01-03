# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:15:13 2018

@author: bianl
"""

#  Assignment 10.2
#  From Course 2: Python Data Structures, Week 6(Chapter 10)
#  IMPORTANT knowledge points:
#  1. dictionary & dict.get() 
#  2. two iterative variables
#  3. 1 line for loop

#  Open file
fname = input("Enter File Name:")
if len(fname) < 1: fname = "mbox-short.txt"
fhand = open(fname)

#  Initialzing
temp = list()
counts = dict()

#  Create dictionary
for line in fhand:
    #  Guardian
    if not line.startswith("From"):
        continue
    
    words = line.split()
    
    #  Guardian
    if len(words) <= 2:
        continue
    #  Message send time
    mst = words[-2].split(':')    
    counts[mst[0]] = counts.get(mst[0],0) + 1

'''
#  Sort and print top10 message send time
for k,v in counts.items():
    newtup = (k,v)
    temp.append(newtup)

temp = sorted(temp)
for k,v in temp:
    print(k,v)
'''
print(sorted([(k,v) for k,v in counts.items() ]))
