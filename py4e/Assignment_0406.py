# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 09:34:13 2018

@author: bianl
"""

#  Assignment 4.6
#  From Course 1: Getting Started with Python, Week 6(Chapter 4)

def computepay(h,r):
    q = h-40
    if q >= 0:
        p=40*r+1.5*r*q
    else:
        p=h*r
    return p

# Get the input from user
hrs=input("Enter Hours:")
h=float(hrs)

rate=input("Enter rate per hour:")
r=float(rate)

# Call computepay function
p = computepay(h,r)

# Output the result
print("Pay",p)
