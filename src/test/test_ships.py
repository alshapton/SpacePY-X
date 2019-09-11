import sys

sys.path.append('../')

from bs4 import BeautifulSoup
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *

api_one_ship_data = ''
api_all_ships_data = ''


def getShipPosition(ship_url):
    soup = BeautifulSoup(makeHTTP(ship_url), 'html.parser')
    for link in soup.find_all('a'):
        l = link.get('href')
        if str(l).startswith('/en/ais/home/centerx'):
            extracted_text = l.replace('center', '').replace('/en/ais/home/', '').replace('/y', '')
            extracted_text = extracted_text[2:extracted_text.find('/zoom')].split(':')
    position = "{'latitude': " + extracted_text[1] + ", 'longitude': " + extracted_text[0] + "}"
    return position


'''
def test_ships(setup_module):
    ships_result=keyOrder(alphaOrder(readJSONFile('ships/all.json')),'ship_id')
    print(api_all_ships_data)
    print(ships_result)
    assert api_all_ships_data == ships_result

def test_one_ship(setup_module):
    one_data=''
    one_result=alphaOrder(readJSONFile('ships/oneshipAMERICANCHAMPION.json'))
    try:
        one_data = alphaOrder(spacexpython.ships.one('AMERICANCHAMPION','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on ships.one('AMERICANCHAMPION")
    api_position=getShipPosition(json.loads(one_data)['url'])
    file_position=json.loads(one_data)['position']
    assert one_data == one_result
    assert False


def test_one_ship_position(setup_module):
    one_data=''
    one_result=alphaOrder(readJSONFile('ships/oneshipAMERICANCHAMPION.json'))
    try:
        one_data = alphaOrder(spacexpython.ships.one('AMERICANCHAMPION','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on ships.one('AMERICANCHAMPION")
    api_position=getShipPosition(json.loads(one_data)['url'])
    file_position=json.loads(one_data)['position']
    assert api_position == file_position
'''


# @pytest.fixture(scope='module')
def test_fred():
    api_all_ships_data = ''
    try:
        api_all_ships_data = keyOrder(alphaOrder(spacexpython.ships.ships('', 1)), 'ship_id')
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on setup of ships test suite")
    print(api_all_ships_data)
    assert False
