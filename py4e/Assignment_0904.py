# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:11:50 2018

@author: bianl
"""

#  Assignment 9.4
#  From Course 2: Python Data Structures, Week 5(Chapter 9)

fname = input('Enter File Name:')
fhand = open(fname)

counts = dict()
maxcounts = None
maxwds = None

for line in fhand:  
    #  Guardian
    if not line.startswith("From"):
         continue
     
    wds = line.split()
    #  Guardian
    if len(wds) <= 2:
        continue
    
    x = wds[1]
    counts[x] = counts.get(x,0) + 1
    if maxcounts is None or counts[x] > maxcounts:
        maxcounts = counts[x]
        maxwds = x
            
print(maxwds,maxcounts)

    