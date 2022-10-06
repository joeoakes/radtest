# Purpose: Mongo class for RadTest
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

#Logging facility for Python
import logging
import sys

class MongoDS:

 def __init__(self, dbname, dbcollection):
  self.dbname = dbname
  self.dbcollection = dbcollection

 def getcontent(self):
  try:
    conn = MongoClient('localhost', 27017)
    db = conn.self.dbname
    col = db.self.dbCollection
    content = col.find_one()
    conn.close()
    return content
  except FileNotFoundError:
    logging.error(str(sys.exc_info()[0]))
