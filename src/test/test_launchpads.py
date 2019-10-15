
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


def test_launchpads():
    launchpads_data = ''
    launchpads_result = keyOrder(
        alphaOrder(readJSONFile('launchpads/all.json')), 'id')
    try:
        launchpads_data = keyOrder(alphaOrder(
            spacexpython.launchpads.launchpads('', 1)), 'id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on launchpads.alllaunchpads")
    assert launchpads_data == launchpads_result


def test_one_launchpad():
    one_data = ''
    one_result = alphaOrder(
        readJSONFile('launchpads/onepad4.json'))
    try:
        one_data = alphaOrder(
            spacexpython.launchpads.one('ksc_lc_39a', '', 1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on launchpads.one('ksc_lc_39a')")
    assert one_data == one_result
