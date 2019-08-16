
import sys
sys.path.append('../')
import spacexpython
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


def test_api():
    api_data=''
    api_result=alphaOrder(readJSONFile('info/api.json'))
    try:
        api_data = alphaOrder(spacexpython.info.api())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.api")
    assert api_result == api_data

def test_company():
    company_data=''
    company_result=alphaOrder(readJSONFile('info/company.json'))
    try:
        company_data = alphaOrder(spacexpython.info.company())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.company")
    assert company_data == company_result
