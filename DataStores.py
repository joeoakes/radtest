#Purpose: Datastores for RadTest
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient
#Logging facility for Python
import logging
import sys

class Json():
 def __init__(self, filename):
   try:
    configs = open(filename, 'r')
    content = configs.read()
    configs.close()
   except:
    logging.error(str(sys.exc_info()[0]))
class MongoDb():
  def __init__(self, dbName, dbCollection):
    try:
     clientDB = MongoClient('localhost', 27017)
     db = clientDB.dbName
     col = db.dbCollection
     clientDB.close()
    except:
        e = sys.exc_info()[0]
        logging.error(str(sys.exc_info()[0]))
class Redis():
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
