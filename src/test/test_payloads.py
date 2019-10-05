
import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

def test_payloads():
    payloads_data=''
    payloads_result=keyOrder(alphaOrder(readJSONFile('payloads/all.json')), 'payload_id')
    try:
        payloads_data = keyOrder(alphaOrder(spacexpython.payloads.payloads('', 1)), 'payload_id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on payloads.allpayloads")
    assert payloads_data == payloads_result


def test_one_payload():
    one_data=''
    one_result = alphaOrder(readJSONFile('payloads/oneTelkom-4.json'))
    try:
        one_data = alphaOrder(spacexpython.payloads.one('Telkom-4', '', 1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on payloads.one('GTO-2')")
    assert one_data == one_result
