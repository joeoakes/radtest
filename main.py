#Purpose: Python3 Web Scraping project for Radwell.
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

# importing python modules
import urllib.request
import json
from bs4 import BeautifulSoup
import sys, datetime

try:
  #JSON Config to work with and open
  configs = open('radscrap.json', 'r')
  content = configs.read()

  # opening the url for reading​
  url = urllib.request.urlopen(json.loads(content))


except:
  e = sys.exc_info()[0]
  print("error: %s" % e)

