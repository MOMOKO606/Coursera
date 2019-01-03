# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:28:32 2018

@author: bianl
"""

#  Assignment 7.2
#  From Course 2: Python Data Structures, Week 3(Chapter 7)

file = input("Enter file name:")
fhandle = open(file)

s = 0
count = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    #  Count number of confidence lines
    count = count+1
    #  Remove whitespace
    line=line.replace(" ","")
    #  Get the :'s index
    p=line.find(":")
    #  Sum the total confidence
    s=s+float(line[p+1:])
           
print("Average spam confidence:",s/count)

