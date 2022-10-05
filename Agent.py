#Agent Class
#Properties Name, ListofWebsites, Starttime, Status, ScrapeTYpe, Database, APIUsed
class Agent:
    def __init__(self,name, listofWebsites, starttime, status, scrapeType, database, apiUsed):
        self.name = name
        self.listofWebsites = listofWebsites
        self.starttime = starttime
        self.status = status
        self.scrapeType = scrapeType
        self.database = database
        self.apiUsed = apiUsed
