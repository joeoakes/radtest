# Purpose: Mongo class for RadTest
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

#Logging facility for Python
import logging
import sys

# make sure to perform pip install pymongo
import pymongo

class MongoDS:

 def getcontent(self, dbname, dbcollection):
  try:
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn[dbname]
    col = db[dbcollection]
    content = col.find()
    conn.close()
    return content
  except pymongo.errors.ConnectionFailure:
    logging.error(str(sys.exc_info()[0]))
