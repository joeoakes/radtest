#Purpose: Python3 Web Scraping project for Radwell.
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

# importing python modules
import urllib.request
import json
from bs4 import BeautifulSoup
import sys, datetime


# Create the json object to 
json = Json('radscrap.json')
content = json.getContent()

  # opening the url for reading
  #url = urllib.request.urlopen(json.loads(content))

