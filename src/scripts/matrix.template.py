import sys
sys.path.append('../')
from tinydb import TinyDB

db = TinyDB('matrixDB.json')      # Connect/Create an existing database
db.purge()                        # If one already exists - purge it.

#  Insert all the matrices for the wrappers into the database


#  Parameters for the info function
db.insert({"function": "info", "subfunction": "clients", "parameters": [{"parameter": "languages", "example": "Python", "type": "str", "comment": "Filter by language(s)"}, {"parameter": "name", "example": "spacex-graphql-rust", "type": "str", "comment": "Filter by Wrapper name"}, {"parameter": "creators", "example": "Or Hiltch", "type": "str", "comment": "Filter by the creator(s) name(s)"}, {"parameter": "repos", "example": "GitHub", "type": "str", "comment": "Filter by repo type"}]})  # noqa
