
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

def test_landingpads():
    landingpads_data=''
    landingpads_result=keyOrder(alphaOrder(readJSONFile('landingpads/all.json')),'id')
    try:
        landingpads_data = keyOrder(alphaOrder(spacexpython.landingpads.landingpads('',1)),'id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on landingpads.alllandingpads")
    assert landingpads_data == landingpads_result


def test_one_landingpad():
    one_data=''
    one_result=alphaOrder(readJSONFile('landingpads/oneASOG.json'))
    try:
        one_data = alphaOrder(spacexpython.landingpads.one('ASOG','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on landingpads.one('ASOG")
    assert one_data == one_result
