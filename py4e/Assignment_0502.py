# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:04:52 2018

@author: bianl
"""

#  Assignment 5.2
#  From Course 1: Getting Started with Python, Week 7(Chapter 5)

# Initailizing the largest & smallest
largest = None
smallest = None

while True:  
    num = input("Enter a number: ")
   
    # Break case    
    if num == "done" :
        break
      
    try:
        # Get the largest & smallest
        num=int(num)
        if largest is None:
            largest = num
        elif num > largest:
            largest =num
   
        if  smallest is None:
            smallest = num  
        elif num < smallest:
            smallest = num
    except:
        # Invalid case
        print("Invalid input")
               
print("Maximum is", largest)
print("Minimum is", smallest)