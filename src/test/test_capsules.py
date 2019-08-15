
import sys
sys.path.append('../')
import spacexpython
from .tutils import *

def test_capsules():
    capsules_result=keyOrder(alphaOrder(readJSONFile('capsules/capsules.json')),'capsule_id')
    capsules_data = keyOrder(alphaOrder(spacexpython.capsules.capsules('',1)),'capsule_id')
    assert capsules_data == capsules_result

def test_upcoming():
    upcoming_result=keyOrder(alphaOrder(readJSONFile('capsules/upcoming.json')),'capsule_id')
    upcoming_data = keyOrder(alphaOrder(spacexpython.capsules.upcoming()),'capsule_id')
    print ("Failure on upcoming capsules")
    assert upcoming_data == upcoming_result


def test_past():
    past_result=keyOrder(alphaOrder(readJSONFile('capsules/past.json')),'capsule_id')
    past_data = keyOrder(alphaOrder(spacexpython.capsules.past()),'capsule_id')
    print ("Failure on past capsules")
    assert past_data == past_result


def test_one():
    one_result=alphaOrder(readJSONFile('capsules/one_C105.json'))
    one_data = alphaOrder(spacexpython.capsules.one('C105'))
    print ("Failure on one capsule (C105)")
    assert one_data == one_result


def test_capsulesP():
    capsulesP_result=alphaOrder(readJSONFile('capsules/capsulesP.json'))
    capsulesP_data = alphaOrder(spacexpython.capsules.capsules('{"capsule_serial":"C112","id":"true"}'))
    print ("Failure on CapsulesP")
    assert capsulesP_data == capsulesP_result
