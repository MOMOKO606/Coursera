# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:49:45 2018

@author: bianl
"""

#  Assignment 7.1
#  From Course 2: Python Data Structures, Week 3(Chapter 7)

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    print(line.rstrip().upper())
    
    
