# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:43:33 2018

@author: bianl
"""

#  Assignment 8.4
#  From Course 2: Python Data Structures, Week 4(Chapter 8)

fhead = open('romeo.txt')
wd=list()  #  Initialized words display list

#  Loop for each line
for line in fhead:
    words=line.split()
    #  Loop for words of each line
    for i in range(len(words)):
        if words[i] not in wd:
            wd.append(words[i])
           
wd.sort()
print(wd)
    