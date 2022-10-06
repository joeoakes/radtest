#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient

class DataStore:
    def connectDatabase(self, databaseType, database, collection):
        if (databaseType == DatabaseTypes.json):
            try:
             configs = open('radscrap.json', 'r')
             content = configs.read()
             configs.close()
             return content
            except:
                e = sys.exc_info()[0]
        elif (databaseType == DatabaseTypes.mongodb):
            try:
             clientDB = MongoClient('localhost', 27017)
             db = clientDB.test_database
            except:
                e = sys.exc_info()[0]
        elif (databaseType == Databases.redis):
            try:
              None
            except:
                e = sys.exc_info()[0]
        elif (databaseType == Databases.cosmos):
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
