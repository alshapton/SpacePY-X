
import sys
sys.path.append('../')
import spacexpython
from .tutils import *

def test_api():
    api_result=alphaOrder(readJSONFile('info/api.json'))
    api_data = alphaOrder(spacexpython.info.api())
    print ("Failure on info.api")
    assert api_result == api_data

def test_company():
    company_result=alphaOrder(readJSONFile('info/company.json'))
    company_data = alphaOrder(spacexpython.info.company())
    print ("Failure on info.company")
    assert company_data == company_result
