#Purpose: Python3 to convert the certificate to hex cert for Bare machine
#Author: Joe Oakes
#Date 10/5/2022

import sys, datetime
#pip install pymongo
from pymongo import MongoClient

try:
    #JSON Config to work with and open
    configs = open('radscrap.json', 'r')
    content = configs.read()

    client = MongoClient('localhost', 27017)
    print("Connected to MongoDB")
    db = client.test_database
    print("Got the Database test_database")
    collection = db.test_collection
    print("Got the Collection")

except:
    e = sys.exc_info()[0]
    print("error: %s" % e)

configs.close()



