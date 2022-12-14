# Purpose: Python3 Web Scraping project for Radwell.
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

# importing python modules
import urllib.request
import json
# from bs4 import BeautifulSoup
import sys
from JsonDS import JsonDS
from MongoDS import MongoDS

jsonDoc = JsonDS('radscrap.json')
content = jsonDoc.getcontent()
print(content)

mongodoc = MongoDS('TestOakes1', 'CollectionOakes')
content = mongodoc.getcontent()
print(content)

  # opening the url for reading
  #url = urllib.request.urlopen(json.loads(content))

