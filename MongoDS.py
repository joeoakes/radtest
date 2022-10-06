# Purpose: Mongo class for RadTest
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

#Logging facility for Python
import logging
import sys

# make sure to perform pip install pymongo
import pymongo

class MongoDS:

 def __init__(self, dbname, dbcollection):
  self.dbname = dbname
  self.dbcollection = dbcollection

 def getcontent(self):
  try:
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn[self.dbname]
    col = db[self.dbcollection]
    content = col.find()
    conn.close()
    return content
  except pymongo.errors.ConnectionFailure:
    logging.error(str(sys.exc_info()[0]))
