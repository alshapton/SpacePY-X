
import sys
sys.path.append('../')
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *



def test_capsules():
    capsules_data=''
    capsules_result=keyOrder(alphaOrder(readJSONFile('capsules/capsules.json')),'capsule_serial')
    try:
        capsules_data = keyOrder(alphaOrder(spacexpython.capsules.capsules('',1)),'capsule_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on Capsules")
    assert capsules_data == capsules_result

def test_upcoming():
    upcoming_data=''
    upcoming_result=keyOrder(alphaOrder(readJSONFile('capsules/upcoming.json')),'capsule_serial')
    try:
        upcoming_data = keyOrder(alphaOrder(spacexpython.capsules.upcoming()),'capsule_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on upcoming capsules")
    assert upcoming_data == upcoming_result


def test_past():
    past_data=''
    past_result=keyOrder(alphaOrder(readJSONFile('capsules/past.json')),'capsule_serial')

    try:
        past_data = keyOrder(alphaOrder(spacexpython.capsules.past()),'capsule_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on past capsules")
    assert past_data == past_result


def test_one():
    one_data=''
    one_result=alphaOrder(readJSONFile('capsules/one_C105.json'))
    try:
        one_data = alphaOrder(spacexpython.capsules.one('C105'))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on one capsule (C105)")
    assert one_data == one_result


def test_capsulesP():
    capsulesP_data=''
    capsulesP_result=alphaOrder(readJSONFile('capsules/capsulesP.json'))
    try:
        capsulesP_data = alphaOrder(spacexpython.capsules.capsules('{"capsule_serial":"C112","id":"true"}'))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on CapsulesP")
    assert capsulesP_data == capsulesP_result
