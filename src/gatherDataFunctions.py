#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys

con = psycopg2.connect(database='testdb')
cur = con.cursor()
itemTable = 'items'
listingTable = 'listings'
transactionTable = 'transactions'


def getAvgSoldPrice(itemName):



def getLeastSolrPrice(itemName):



def highestSoldPrice(itemName):



def lowestCurrentPrice(itemName):



def highestCurrentPrice(itemName):
