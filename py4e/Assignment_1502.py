# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:55:29 2018

@author: bianl
"""

#  Assignment 15.2 Counting Email in a Database
#  From Course 4: Using Databases with Python, Week 2(Chapter 15)
#  IMPORTANT knowledge points:
#  1. sqlite3
#  2. connect, cursor, execute
#  3. commit
#  4. INSERT, SELECT, UPDATE, WHERE, ORDER BY

import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    org = tuple(re.findall('@(\S+)',line))
#   pieces = line.split()
#   org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', org)
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', org)
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    org)
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
