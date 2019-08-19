
import sys
sys.path.append('../')
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


def test_rockets():
    rockets_data=''
    rockets_result=keyOrder(alphaOrder(readJSONFile('rockets/all.json')),'rocket_id')
    try:
        rockets_data = keyOrder(alphaOrder(spacexpython.rockets.all('',1)),'rocket_id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on all rockets")
    assert rockets_data == rockets_result

def test_rocketsP():
    rockets_data=''
    rockets_result=keyOrder(alphaOrder(readJSONFile('rockets/all_limit1.json')),'rocket_id')
    try:
        rockets_data = keyOrder(alphaOrder(spacexpython.rockets.all('{"limit":"1"}',1)),'rocket_id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on all rockets")
    assert rockets_data == rockets_result


def test_rocketF1():
    f1_data=''
    f1_result=alphaOrder(readJSONFile('rockets/falcon1.json'))
    try:
        f1_data = alphaOrder(spacexpython.rockets.rocket('falcon1','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on Falcon1")
    assert f1_data == f1_result


def test_rocketF9():
    f9_data=f9_result=alphaOrder(readJSONFile('rockets/falcon9.json'))
    try:
        f9_data = alphaOrder(spacexpython.rockets.rocket('falcon9','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on Falcon9")
    assert f9_data == f9_result


def test_rocketBFR():
    bfr_data=''
    bfr_result=alphaOrder(readJSONFile('rockets/BFR.json'))
    try:
        bfr_data = alphaOrder(spacexpython.rockets.rocket('bfr','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.api")
    assert bfr_data == bfr_result


def test_rocketFH():
    fh_data=''
    fh_result=alphaOrder(readJSONFile('rockets/falconheavy.json'))
    try:
        fh_data = alphaOrder(spacexpython.rockets.rocket('falconheavy','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on Falcon Heavy")
    assert fh_data == fh_result
