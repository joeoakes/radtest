#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#make sure to perform pip install pymongo
from pymongo import MongoClient

class DataStore:
    def connectDatabase(self, databaseType, database, collection):
        if (databaseType == Databases.mongodb):
            clientDB = MongoClient('localhost', 27017)
        elif (databaseType == Databases.redis):
             None
        elif (databaseType == Databases.mongodb):
            None
    def getResourceById(self, resourceId):
        self.get(resourceId)
    def setResource( resourceId, resourceContent):
        None
        # TODO:
        #self[resourceId] = resourceContent

  db = clientDB.test_database
  print("Got the Database test_database")
  collection = db.test_collection
  print("Got the Collection")

  #Teardown Section
  configs.close()
  clientDB.close()