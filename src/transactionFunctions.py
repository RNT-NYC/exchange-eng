#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys

con = psycopg2.connect(database='testdb')
cur = con.cursor()
itemTable = 'items'
listingTable = 'listings'
transactionTable = 'transactions'

def transactionMade(transactionInfo):
    """
        This function creates a transaction between two users
        This will update the listing tobeing sold through the function listingSold()

        Args:
            transactionInfo: a list that contains all the information possible to create the transaction

        Return:
            transaction will have been madeand the listing will have been updated
    """
    verified = verifyTransaction(transactionInfo)
    if verified:
        cleanedList = cleanInfo(transactionInfo)
        cur.execute("INSERT INTO " + transactionTable + "VALUES(" + cleanedList[0] + "," + cleanedList[1]
        + "," + cleanedList[2] + "," + cleanedList[3] + "," + cleanedList[4] + "," + cleanedList[5] +
        "," + cleanedList[6] + "," + cleanedList[7] + "," + cleanedList[8] + "," + cleanedList[9] +
        "," +")")
        listingSold(cleanedList[4])



def transactionCanceled(transactionID):
    """
        This fuction cancels a transaction just in case a user decides to cancel an order
        we still want to keep record of the transaction however so we simply flip a boolean

        Args:
            transactionID: the ID of the transaction we wish to switch

        Return:
            transaction will have changed to false, and the listting 'sold' will be reversed
    """
    cur.execute('SELECT EXISTS(select 1 from' + transactionTable +'where ID =' +transactionID + ')')
    verfied = cur.fetchone()
    if verified:
        cur.execute("UDPATE" + transactionTable+ "SET isValid = FALSE WHERE ID =" +transactionID + ')')
        cur.execute("SELECT listingID FROM "+ transactionTable + " WHERE transactionID = " + transactionID)
        listingID = cur.fetchone()
        listingsoldReverse(listingID)





def listingSold(listingID):
    """
        This function changes a entry in the listings table to mark it as sold
        so it willl no longer display on the page

        Args:
            listingID: The ID for the listing that will be in the table

        Return:
            The listing will have been updated to be unavailable
    """
    cur.execute("UPDATE" + listingTable + "SET onSale = FALSE WHERE listingID = "+ listingID)


def listingSoldReverse(listingID):
    """
        This funcction will change an entry in the listing table to marke it as
        still available so it will display on the views page

        Args:
            listingID: THe ID for the listing that will be changed

        Return:
            The listing will have been updated to be available
    """
    cur.execute("UPDATE" + listingTable + "SET onSale = TRUE WHERE listingID = "+ listingID)




def cleanInfo(infoList):
    """
        This function cleans our lists so they are ready to be placed in our database since postgres
        has strict rules as to what constitutes as values within tables
        This function should always be used before inputing information into the database.

        Args:
            infoList: the list that needs to be  cleaned.

        Return:
            infoList: the cleaned list.
    """


    for info in infoList:
        if (isinstance(info,str)):
            info = "'" + info + "'"
    return infoList




def verifyTransaction(transactionInfo):
    """
        This function verifies that all the information placed in the list transactionInfo is correct.

        Args:
            transactionInfo: a list that contains all of the information needed to create a new entry in the
            transations table within our database

        Return:
            boolean: true if the transacction information is verified and and error if there is an incosistency.
    """
    if len(itemInfo != 11):
        raise ValueError('The amount of information put for this item is incorrect. Please check again that you inputed the correct values for the transaction.')
    if (!isinstance(itemInfo[0],int)):====
        raise ValueError("A integer wasn't enetered for the ID of the transaction. Please verify that all information placed is correct")
    if (!isinstance(itemInfo[1],int)):
        raise ValueError("A integer wasn't entered for the SellerID of the transaction. Please verify that all information placed is correct")
    if(!isinstance(itemInfo[2],int)):
        raise ValueError("A integer wasn't entered for the BuyerID of the transaction. Please verify that all information placed is correct")
    if(!isinstance(itemInfo[3],int)):
        raise ValueError("A integer wasn't entered for the amount of money exchanged for this transaction.  Please verify that all information placed for the item is correct.")
    if(!isinstance(itemInfo[4],int)):
        raise ValueError("A integer wasn't entered for the listingID of the transaction.  Please verify that all information placed for item is correct.")
    if(!isinstance(itemInfo[5],str)):
        raise ValueError("A string wasn't entered for the delivery address of the transaction. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[6],str)):
        raise ValueError("A string wasn't entered for the sender's address of the transaction. Please verify that all information placed for item is correct.t")
    if(isinstance(itemInfo[7],str)):
        raise ValueError("A date wasn't entered for the time fo sale for the transaction. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[8],int)):
        raise ValueError("A integer wasn't entered for the rating of the seller for this transaction. Please verify that all information placed for item is correct.t")
    if(isinstance(itemInfo[9],int)):
        raise ValueError("An integer wasn't entered for the rating of the buyer for this transaction. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[10],int)):
        raise ValueError("An boolean wasn't entered for the validity of the . Please verify that all information placed for item is correct.")
    return True
