
import sys
sys.path.append('../')
import spacexpython
from .tutils import *

def test_launches():
    launches_result=keyOrder(alphaOrder(readJSONFile('launches/all.json')),'flight_number')
    launches_data = keyOrder(alphaOrder(spacexpython.launches.all('',1)),'flight_number')
    assert launches_data == launches_result
