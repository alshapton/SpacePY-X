
import sys
sys.path.append('../')
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


def test_cores():
    cores_data = ''
    cores_result = keyOrder(alphaOrder(readJSONFile(
        'cores/cores.json')), 'core_serial')
    try:
        cores_data = keyOrder(alphaOrder(
            spacexpython.cores.cores('', 1)), 'core_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on cores")
    assert cores_data == cores_result


def test_upcoming():
    upcoming_data = ''
    upcoming_result = keyOrder(alphaOrder(readJSONFile(
        'cores/upcoming.json')), 'core_serial')
    try:
        upcoming_data = keyOrder(alphaOrder(
            spacexpython.cores.upcoming()), 'core_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on upcoming cores")
    assert upcoming_data == upcoming_result


def test_past():
    past_data = ''
    past_result = keyOrder(alphaOrder(readJSONFile(
        'cores/past.json')), 'core_serial')
    try:
        past_data = keyOrder(alphaOrder(
            spacexpython.cores.past()), 'core_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on past cores")
    assert past_data == past_result


def test_one():
    one_result = alphaOrder(readJSONFile(
        'cores/one_B1032.json'))
    try:
        one_data = alphaOrder(spacexpython.cores.one('B1032'))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on one core (B1032)")
    assert one_data == one_result


def test_coresP():
    coresP_data = ''
    coresP_result = alphaOrder(readJSONFile
                               ('cores/coresP.json'))
    try:
        coresP_data = alphaOrder(
            spacexpython.cores.cores(
                '{"core_serial":"B1037","block":"3"}'))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on coresP")
    assert coresP_data == coresP_result
