# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:24:46 2018

@author: bianl
"""

#  Assignment 3.3
#  From Course 1: Getting Started with Python, Week 5(Chapter 3)

score = input("Enter Score: ")
# convert the type of input
try:
    score = float(score)
except:
    print("Error, Please enter numeric input")

# calculate the grade of score
if score > 1.0:
    print ("Error")
elif score >= 0.9:
    grade='A'
elif score >= 0.8:
    grade='B'
elif score >= 0.7:
    grade='C'
elif score >= 0.6:
    grade='D'   
else:
    grade='F' 

# output the result
print(grade)
    