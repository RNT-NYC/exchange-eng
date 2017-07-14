#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = psycopg2.connect(database='testdb')
cur = con.cursor()
#cur.execute('SELECT version()')
#ver = cur.fetchone()
#print (ver)
itemTable = 'items'
listingTable = 'listings'
cur.execute('SELECT name FROM ' + itemTable)
#trvar = str(cur.fetchone())
#strvar = strvar[2:-3]


nameList = str(cur.fetchall())
nameList = nameList.split(')')
for i in range(len(nameList)):
    if (i == 0):
        nameList[i] = nameList[i][3:-2]
    else:
        nameList[i] = nameList[i][4:-2]
    print (nameList[i])

name = "Fuck The President Supreme T-Shirt"
name = "'" + name + "'"
cur.execute("SELECT EXISTS (SELECT 1 FROM " + itemTable + " WHERE name = " +name + ")")
yes =  cur.fetchone()
if yes:
    print('hi')
else:
    print('no')


#print(strvar)
print('test')
