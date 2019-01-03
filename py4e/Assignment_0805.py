# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:04:54 2018

@author: bianl
"""
#  Assignment 8.5
#  From Course 2: Python Data Structures, Week 4(Chapter 8)

al = list()
count = 0

fh = open("mbox-short.txt")
for line in fh:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 2:
            al.append(words[1])
            count=count+1  
            
for i in range(len(al)):
    print(al[i])
print("There were", count, "lines in the file with From as the first word")
