


import sys
sys.path.append('../')
sys.path.append('../spacexpython/')
from tinydb import TinyDB, Query
from exceptions import *

import json
import ast

db = TinyDB('matrix.json')      # Connect/Create an existing database
db.purge()                      # If one already exists - purge it.

# Insert all the matrices for the wrappers into the database
db.insert({"function":"capsules","subfunction":"capsules","parameters":[{"parameter":"capsule_serial","example":"C112","type":"str","comment":"Filter by capsule serial number"},{"parameter":"capsule_id","example":"dragon1","type":"str","comment":"Filter by capsule id"},{"parameter":"status","example":"active","type":"str","comment":"Filter by capsule status"},{"parameter":"original_launch","example":"2017-02-19T14:39:00.000ZUTC ISO","type":"timestamp","comment":"Filter by capsule original launch date"},{"parameter":"mission","example":"SpaceX CRS-5","type":"str","comment":"Filter by capsule mission"},{"parameter":"landings","example":"2","type":"int","comment":"Filter by capsule landings"},{"parameter":"type","example":"Dragon 1.1","type":"str","comment":"Filter by capsule type"},{"parameter":"reuse_count","example":" 1","type":"int","comment":"Filter by number of times the capsule was reused"},{"parameter":"id","example":"true","type":"bool","comment":"Set as true to show mongo document id's"},{"parameter":"limit","example":"3","type":"int","comment":"Limit results returned, defaults to all documents returned"},{"parameter":"offset","example":"3","type":"int","comment":"Offset or skip results from the beginning of the query"},{"parameter":"sort","example":"capsule_serial","type":"str","comment":"Change result sorting by setting value to any parameter in this list"},{"parameter":"order","example":"desc","type":"str","comment":"Change result ordering by setting values of asc or desc"}]})
db.insert({"function":"capsules","subfunction":"one","parameters":[{"parameter":"capsule_serial","example":"C112","type":"str","comment":"Filter by capsule serial number"},{"parameter":"id","example":"true","type":"bool","comment":"Set as true to show mongo document ids"}]})




