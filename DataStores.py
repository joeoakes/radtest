#Purpose: Datastores for RadTest
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient
#Logging facility for Python
import logging
import sys

class Redis(dbname, dbcollection):
 def __init__(self):
    try:
     None
    except:
     logging.error(str(sys.exc_info()[0]))
 def getResourceById(self, resourceId):
   self.get(resourceId)
 def setResource( resourceId, resourceContent):
  None
   # TODO:
   #self[resourceId] = resourceContent
