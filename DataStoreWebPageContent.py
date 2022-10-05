#Purpose: Datastore for WebPage content
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

class DataStoreWebPageContent:
    def __init__(self, resourceId, resourceContent):
        self.resourceId = resourceId
        self.resourceContent =  resourceContent
    def connectDatabase(self, ):
    def getResourceById(self, resourceId):
        #GET
        self.get(resourceId)
    def setResource( resourceId, resourceContent):
        #SET
        #self[resourceId] = resourceContent