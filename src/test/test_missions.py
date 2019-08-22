
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

def test_missions():
    missions_data=''
    missions_result=keyOrder(alphaOrder(readJSONFile('missions/all.json')),'mission_id')
    try:
        missions_data = keyOrder(alphaOrder(spacexpython.missions.missions('',1)),'mission_id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on missions.allmissions")
    assert missions_data == missions_result

def test_one_mission():
    one_data=''
    one_result=alphaOrder(readJSONFile('missions/oneF3364BF.json'))
    try:
        one_data = alphaOrder(spacexpython.missions.one('F3364BF','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        #pytest.xfail("Space/X API Read Timed Out")
        print("Failure on missions.one('F3364BF')")
    assert one_data == one_result
