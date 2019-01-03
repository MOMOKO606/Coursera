# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:25:51 2018

@author: bianl
"""

#  Assignment 12.1 Understanding the Request / Response Cycle
#  From Course 3: Using Python to Access Web Data, Week 3(Chapter 12)
#  IMPORTANT knowledge points:
#  1. socket
#  2. encode & decode

import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()