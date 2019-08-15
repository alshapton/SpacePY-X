
import sys
sys.path.append('../')
import spacexpython
from .tutils import *


def test_rockets():
    rockets_result=keyOrder(alphaOrder(readJSONFile('rockets/all.json')),'rocket_id')
    rockets_data = keyOrder(alphaOrder(spacexpython.rockets.all('',1)),'rocket_id')
    print ("Failure on all rockets")
    assert rockets_data == rockets_result

def test_rocketsP():
    rockets_result=keyOrder(alphaOrder(readJSONFile('rockets/all_limit1.json')),'rocket_id')
    rockets_data = keyOrder(alphaOrder(spacexpython.rockets.all('{"limit":"1"}',1)),'rocket_id')
    print ("Failure on all rockets")
    assert rockets_data == rockets_result


def test_rocketF1():
    f1_result=alphaOrder(readJSONFile('rockets/falcon1.json'))
    f1_data = alphaOrder(spacexpython.rockets.rocket('falcon1','',1))
    print ("Failure on Falcon1")
    #assert 1==1
    assert f1_data == f1_result


def test_rocketF9():
    f9_result=alphaOrder(readJSONFile('rockets/falcon9.json'))
    f9_data = alphaOrder(spacexpython.rockets.rocket('falcon9','',1))
    print ("Failure on Falcon9")
    assert f9_data == f9_result


def test_rocketBFR():
    bfr_result=alphaOrder(readJSONFile('rockets/BFR.json'))
    bfr_data = alphaOrder(spacexpython.rockets.rocket('bfr','',1))
    print ("Failure on BFR")
    assert bfr_data == bfr_result


def test_rocketFH():
    fh_result=alphaOrder(readJSONFile('rockets/falconheavy.json'))
    fh_data = alphaOrder(spacexpython.rockets.rocket('falconheavy','',1))
    print ("Failure on Falcon Heavy")
    assert fh_data == fh_result
