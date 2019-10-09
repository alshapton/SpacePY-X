import sys
sys.path.append('../')
from tinydb import TinyDB

db = TinyDB('matrixDB.json')      # Connect/Create an existing database
db.purge()                      # If one already exists - purge it.

# Insert all the matrices for the wrappers into the database

