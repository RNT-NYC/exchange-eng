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
    """
        This function will get the Average Sold Price for an item by running a query through transactions
        table

        Args:
            itemName: The name of the item we wish to find the avg sold price for

        Return:
            will update the item's row to import the new average sold price
    """


def getLeastSolrPrice(itemName):
    """
        This function will get the Least Sold Price for an item by running a query through transactions
        table

        Args:
            itemName: The name of the item we wish to find the least sold price for

        Return:
            will update the item's row to import the new least sold price
    """


def highestSoldPrice(itemName):
    """
        This function will get the Highest Sold Price for an item by running a query through transactions
        table

        Args:
            itemName: The name of the item we wish to find the highest sold price for

        Return:
            will update the item's row to import the new highest sold price
    """


def lowestCurrentPrice(itemName):
    """
        This function will get the lowest current price for an item by running a query through transactions
        table

        Args:
            itemName: The name of the item we wish to find the lowest current price for

        Return:
            will update the item's row to import the new lowest current price
    """


def highestCurrentPrice(itemName):
    """
        This function will get the highest current price for an item by running a query through transactions
        table

        Args:
            itemName: The name of the item we wish to find the highest current price for

        Return:
            will update the item's row to import the new highest current price
    """
