# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:32:50 2018

@author: bianl
"""

#  Assignment 11.1 Extracting Data With Regular Expressions
#  From Course 3: Using Python to Access Web Data, Week 2(Chapter 11)
#  IMPORTANT knowledge points:
#  1. Regular expressions
#  2. 1 line for loop

import re

fname = input('Enter File Name:')
if len(fname) < 1: fname = 'test02.txt'
fhand = open(fname)

total_line = 0.0
for line in fhand:
    line = line.rstrip()
    tmp = re.findall("[0-9]+",line)
    #  String 2 float, All Number From The Line
    anftl = [float(tmp[i]) for i in range(len(tmp))]
    #  Counting
    line_sum = sum(anftl)
    total_line = total_line + line_sum
    
print(total_line)