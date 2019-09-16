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
    position = '{"latitude": ' + extracted_text[1] + ', "longitude": ' + extracted_text[0] + '}'
    return position

def test_one_ship_position():
    one_data=''
    one_result=alphaOrder(readJSONFile('ships/oneshipAMERICANCHAMPION.json'))
    try:
        one_data = alphaOrder(spacexpython.ships.one('AMERICANCHAMPION','',1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on ships.one('AMERICANCHAMPION")
    one_result=getShipPosition(json.loads(one_data)['url'])
    file_lat=json.loads(one_data)['position']['latitude']
    file_long=json.loads(one_data)['position']['longitude']
    api_lat = json.loads(one_result)['latitude']
    api_long = json.loads(one_result)['longitude']
    assert ((minus_percent(1, file_lat) <= api_lat <= plus_percent(1, file_lat)) or (minus_percent(1, file_long) <= api_long <= plus_percent(1, file_long))) \
        or ((minus_percent(1, file_lat) >= api_lat >= plus_percent(1, file_lat)) or (minus_percent(1, file_long) >= api_long >= plus_percent(1, file_long)))  \
        or ((minus_percent(1, file_lat) >= api_lat >= plus_percent(1, file_lat)) or (minus_percent(1, file_long) <= api_long <= plus_percent(1, file_long))) \
        or ((minus_percent(1, file_lat) <= api_lat <= plus_percent(1, file_lat)) or (minus_percent(1, file_long) >= api_long >= plus_percent(1, file_long)))

def test_all_ships():
    api_all_ships_data = ''
    ships_result = keyOrder(alphaOrder(readJSONFile('ships/all.json')), 'ship_id')
    try:
        api_all_ships_data = alphaOrder(spacexpython.ships.ships())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on setup of ships test suite")
    api_all_ships_data=keyOrder(api_all_ships_data,'ship_id')
    assert api_all_ships_data == ships_result


