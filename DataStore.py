#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient

class DataStore():
    def __init__(self, databaseType, databaseName, databaseCollection):
        self.databaseType = databaseType
        self.databaseName = databaseName
        self.databaseCollection = databaseCollection
class Json(DataStore):
    try:
        configs = open('radscrap.json', 'r')
        content = configs.read()
        configs.close()
    except:
        e = sys.exc_info()[0]
class MongoDb(DataStore):
    try:
        clientDB = MongoClient('localhost', 27017)
        db = clientDB.test_database
    except:
        e = sys.exc_info()[0]
class Redis(DataStore):
    try:
        None
    except:
        e = sys.exc_info()[0]

    def getResourceById(self, resourceId):
        self.get(resourceId)
    def setResource( resourceId, resourceContent):
        None
        # TODO:
        #self[resourceId] = resourceContent
