# Purpose: JSON class for RadTest
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

#Logging facility for Python
import logging
import sys

class JsonDS:

 def __init__(self, filename):
  self.filename = filename

 def getcontent(self):
  try:
    jfile = open(self.filename, 'r')
    content = jfile.read()
    jfile.close()
    return content
  except FileNotFoundError:
    logging.error(str(sys.exc_info()[0]))
