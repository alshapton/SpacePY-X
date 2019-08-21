
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

def test_dragons():
    dragons_data=''
    dragons_result=keyOrder(alphaOrder(readJSONFile('dragons/all.json')),'id')
    try:
        dragons_data = keyOrder(alphaOrder(spacexpython.dragons.dragons('',1)),'id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on dragons.alldragons")
    assert dragons_data == dragons_result

def test_one_dragon():
    one_data=''
    one_result=alphaOrder(readJSONFile('dragons/onedragon1.json'))
    try:
        one_data = alphaOrder(spacexpython.dragons.one('dragon1','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on dragons.one('dragon1")
    assert one_data == one_result

