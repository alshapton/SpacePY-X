import sys
sys.path.append('../')

import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


@pytest.mark.skip(reason="Skip - history changes over time")
def test_history():
    history_data = ''
    history_result = keyOrder(alphaOrder(
        readJSONFile('history/all.json')), 'id')
    try:
        history_data = alphaOrder(
            spacexpython.history.history('', 1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on history.allhistory")
    assert history_data == history_result


def test_one_history():
    one_data = ''
    one_result = alphaOrder(
        readJSONFile('history/one.json'))
    try:
        one_data = alphaOrder(spacexpython.history.one('1', '', 1))
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on history.one('dragon1")
    assert one_data == one_result
