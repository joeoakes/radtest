#Purpose: JSON class for RadTest
#Author: Joe Oakes, Hof Uni, PSA
#Date 10/5/2022

#Logging facility for Python
import logging
import sys


class JsonDS:
 def __init__(self, filename):
   try:
    configs = open(filename, 'r')
    content = configs.read()
    configs.close()
   except:
    logging.error(str(sys.exc_info()[0]))
 def getcontent(self):
     return self.content