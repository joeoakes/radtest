#Purpose: Agent class
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

class Agent:
    def __init__(self,name, pid, pscript, listofWebsites, starttime, status, scrapeType, database, apiUsed):
        self.name = name
        self.pid = pid  #process identifier
        self.pscript = pscript #python script to run
        self.listofWebsites = listofWebsites
        self.starttime = starttime
        self.status = status
        self.scrapeType = scrapeType
        self.database = database
        self.apiUsed = apiUsed
