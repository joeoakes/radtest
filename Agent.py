#Purpose: Agent class
#Author: Joe Oakes
#Date 10/5/2022

class Agent:
    def __init__(self,name, listofWebsites, starttime, status, scrapeType, database, apiUsed):
        self.name = name
        self.listofWebsites = listofWebsites
        self.starttime = starttime
        self.status = status
        self.scrapeType = scrapeType
        self.database = database
        self.apiUsed = apiUsed
