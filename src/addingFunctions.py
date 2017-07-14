#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys

con = psycopg2.connect(database='testdb')
cur = con.cursor()
itemTable = 'items'
listingTable = 'listings'


def verifyAddListings(listingInfo):
        """
            This function will validate that the item name exists within our database.
            if the item does not exists witin the database then we will create a new item
            and then add the listing to that item
        Args:
            listingInfo: a python list that contains all the information needed for a listing
        Return:
            A boolean true or false that will be passedon to the function createListing and will
            whether or not we will successfully create the listing or create a new item first.
        """

    name = listingInfo[1]
    name = "'" + name + "'"
    cur.execute("SELECT EXISTS (SELECT 1 FROM" + itemTable + "WHERE name =" + name + ")")
    inDB = cur.fetchone()
    if inDB:
        return True
    else:
        return False



def createListing(listingInfo):
        """
            This function will first call upon verifyAddListings then it will either/or create a new item as well
            as a listing.
        Args:
            listingInfo: A list containing everything for an entry in the database

        Return:
            Null, but by the end either an error is raised or a new entry in the database should be created.

        """
        verified = verifyListing(listingInfo)
        if verified:
            secondVerify = verifyAddListings(listingInfo)
            if secondVerify:
                cleanedList = cleanInfo(listingInfo)
                cur.execute("INSERT INTO " + listingTable + "VALUES(" + cleanedList[0] + "," + cleanedList[1]
                + "," + cleanedList[2] + "," + cleanedList[3] + "," + cleanedList[4] + "," + cleanedList[5] +
                 "," + cleanedList[6] + "," + cleanedList[7] + "," +")")
            else:
                #prompt the user to create the new item
                #then add the listing.





def createItem(itemInfo):
    """
        This function will create a new entry in the Item Table within our database


        Args:
            itemInfo: A list that contains all of the informationneeded to create a new entry within the
            database

        Return:
            Null, but by the end of this either an error is returned or a new entry in the database
    """

    verified = verifyItem(itemInfo)
    if verified:
        cleanedList = cleanInfo(infoList)
        cur.execute("INSERT INTO " + itemTable + "VALUES(" + cleanedList[0] + "," + cleanedList[1]
        + "," + cleanedList[2] + "," + cleanedList[3] + "," + cleanedList[4] + "," + cleanedList[5] +
         "," + cleanedList[6] + "," + cleanedList[7] + "," + cleanedList[8] + "," + cleanedList[9] +
         "," + cleanedList[10] + "," +")")



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



def verifyListing(listingInfo):
        """
            This function verifies the listing to make sure the data being placed within the function is correct.
            raises an error if there data isn't correct

            Args:
                listingInfo: the list that contains all of the different data

            Return:
                boolean: true or an error depending if the data is correct or not.
        """
    if len(listingInfo != 8):
        raise ValueError('The amount of information put for this Listing is incorrect. Please check again that you inputed the correct values for this list.')
    if (!isinstance(listingInfo[0],int)):
        raise ValueError("An integer wasn't entered for ID. Please verify that all the information placed is correct")
    if (!isinstance(listingInfo[1],str)):
        raise ValueError("A string was not entered for the Name of item for the listing. Please verify that all the information placed is correct")
    if(!isinstance(listingInfo[2],int)):
        raise ValueError("A integer was not entered for price of the listing. Pleasse verify that all the information placed is correct")
    if(!isinstance(listingInfo[3],str)):
        raise ValueError("A string was not entered for the size of the product within the listing. Please verify that all the information placed is correct")
    if(!isinstance(listingInfo[4],str)):
        raise ValueError("A string was not entered for the description of the product within the listing. Please verify that all the information placed is correct]")
    if(!isinstance(listingInfo[5], int))
        raise ValueError("Please make sure that the correct id is placed for the seller of the user. Verify that all information placed is correct")
    if(!isinstance(listingInfo[6],int)):
        raise ValueError("For condition please choose a value between 0-10. Verify that all information placed is correct")
    if(isinstance(listingInfo[7],bool)):
        raise ValueError("onSale should be a boolean type, please verify that all information is correct")
    return True



def verifyItem(itemInfo):
    """
        This function verifies the item data being presented is correct. If it is not
        an error will be raised.

        Args:
            itemInfo: the list that contains all the information that is going to be placed in an item entry

        Return:
            boolean: true or an error depending if the data is correct or not.
    """
    if len(itemInfo != 11):
        raise ValueError('The amount of information put for this item is incorrect. Please check again that you inputed the correct values for this list.')
    if (!isinstance(itemInfo[0],str)):
        raise ValueError("A string wasn't entered for the item name. Please verify that all information placed for item is correct.")
    if (!isinstance(itemInfo[1],str)):
        raise ValueError("A sring wasn't entered for the item description. Please verify that all information placed is correct.")
    if(!isinstance(itemInfo[2],int)):
        raise ValueError("A string wasn't entered for the materal description.  Please verify that all information placed for item is correct.")
    if(!isinstance(itemInfo[3],str)):
        raise ValueError("A string wasn't entered for the category description. Please verify that all information placed for the item is correct.")
    if(!isinstance(itemInfo[4]str)):
        raise ValueError("A string wasn't entered for the subcategory description.  Please verify that all information placed for item is correct.")
    if(!isinstance(itemInfo[5],str)):
        raise ValueError("A string wasn't entered for the brand name. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[6],int)):
        raise ValueError("A integer wasn't entered for the avgSoldPrice. Please verify that all information placed for item is correct.t")
    if(isinstance(itemInfo[7],int)):
        raise ValueError("An integer wasn't entered for leastSoldPrice. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[8],int)):
        raise ValueError("A integer wasn't entered for the highestSoldPrice. Please verify that all information placed for item is correct.t")
    if(isinstance(itemInfo[9],int)):
        raise ValueError("An integer wasn't entered for lowestCurrentPrice. Please verify that all information placed for item is correct.")
    if(isinstance(itemInfo[10],int)):
        raise ValueError("An integer wasn't entered for highestCurrentPrince. Please verify that all information placed for item is correct.")
    return True
