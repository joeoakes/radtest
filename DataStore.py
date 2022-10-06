#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient
#Logging facility for Python
import logging

class DataStore():
    def __init__(self, name, collection):
        self.name = name
        self.collection = collection
class Json(DataStore):
    try:
        configs = open(name, 'r')
        content = configs.read()
        configs.close()
    except:
        logging.error(sys.exc_info()[0])
class MongoDb(DataStore):
    try:
        clientDB = MongoClient('localhost', 27017)
        db = clientDB.name
        col = db.collection
    except:
        logging.error(sys.exc_info()[0])
class Redis(DataStore):
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
