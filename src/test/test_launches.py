
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

def test_launches():
    launches_data=''
    launches_result=keyOrder(alphaOrder(readJSONFile('launches/all.json')),'flight_number')
    try:
        launches_data = keyOrder(alphaOrder(spacexpython.launches.alllaunches('',1)),'flight_number')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on launches.all")
    assert launches_data == launches_result
