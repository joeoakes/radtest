#Purpose: Python3 to convert the certificate to hex cert for Bare machine
#Author: Joe Oakes
#Date 10/5/2022

# importing python modules
import urllib.request
import json
from bs4 import BeautifulSoup
import sys, datetime
#make sure to perform pip install pymongo
from pymongo import MongoClient

try:
  #JSON Config to work with and open
  configs = open('radscrap.json', 'r')
  content = configs.read()

  # opening the url for reading​
  url = urllib.request.urlopen(json.loads(content))

  #Connect to the MongoDB Database
  clientDB = MongoClient('localhost', 27017)
  print("Connected to MongoDB")
  db = clientDB.test_database
  print("Got the Database test_database")
  collection = db.test_collection
  print("Got the Collection")

  #Teardown Section
  configs.close()
  clientDB.close()

except:
  e = sys.exc_info()[0]
  print("error: %s" % e)

