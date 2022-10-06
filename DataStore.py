#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient
#Logging facility for Python
import logging
import sys

class DataStore():
    def __init__(self, name, collection):
        self.name = name
        self.collection = collection
class Json(DataStore):
    def __init__(self):
      try:
        configs = open(self.name, 'r')
        content = configs.read()
        configs.close()
      except:
        e = sys.exc_info()[0]
        logging.error(e)
class MongoDb(DataStore):
  def __init__(self):
    try:
        clientDB = MongoClient('localhost', 27017)
        db = clientDB.self.name
        col = db.self.collection
        clientDB.close()
    except:
        e = sys.exc_info()[0]
        logging.error(e)
class Redis(DataStore):
    def __init__(self):
      try:
        None
      except:
        logging.error(ys.exc_info()[0])
    def getResourceById(self, resourceId):
        self.get(resourceId)
    def setResource( resourceId, resourceContent):
        None
        # TODO:
        #self[resourceId] = resourceContent
