
import sys
sys.path.append('../')
import pytest
import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *


def test_crew():
    crew_data=''
    crew_result='[]'
    try:
        crew_data = alphaOrder(spacexpython.crew.crew())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on Crew")
    assert crew_result == crew_data
