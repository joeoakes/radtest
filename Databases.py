# Purpose: Enumerations for Database types
# Author: Joe Oakes, Hof Uni, PSA
# Date 10/5/2022

import enum

class DatabasesTypes(enum.Enum):
 json = 1
 mongodb = 2
 redis = 3
 cosmos = 4

class Databases(enum.Enum):
 radConfig = 1
 radWebContent = 2
