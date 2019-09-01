import sys

sys.path.append('../')
import pytest

import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *
import subprocess
from time import gmtime, strftime
from datetime import timedelta, datetime

# Conversion factors:
# Kilometers to Miles
# Astronomical Units to Kilometres
KM_TO_MILES = 0.621371
AU_TO_KM = 149598073.0

# Date strings
NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
END = datetime.now() + timedelta(days=1)
TOMORROW = END.strftime('%Y-%m-%d %H:%M:%S')

# Base directory for API-sourced data
BASE='data/roadster/roadster.'


def test_mars_distance_km(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"]) <= json.loads(setup_module)[
        "API_mars_distance_km"] <= plus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"])


def test_mars_distance_mi(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"]) <= json.loads(setup_module)[
        "API_mars_distance_mi"] <= plus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"])


def test_orbital_speed_kph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_kph"]) <= json.loads(setup_module)[
        "API_speed_kph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_kph"])


def test_orbital_speed_mph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_mph"]) <= json.loads(setup_module)[
        "API_speed_mph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_mph"])

def test_epoch(setup_module):
    assert json.loads(setup_module)["LCL_epoch"] == json.loads(setup_module)["API_epoch"]


@pytest.fixture(scope='module')
def setup_module():
    CDATA = ""

    try:
        roadster_data = alphaOrder(spacexpython.roadster.roadster())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.roadster")

    mars_distance_from_api_km = (json.loads(roadster_data)["mars_distance_km"])
    mars_distance_from_api_mi = (json.loads(roadster_data)["mars_distance_mi"])

    orbital_speed_kph = (json.loads(roadster_data)["speed_kph"])
    orbital_speed_mph = (json.loads(roadster_data)["speed_mph"])

    epoch_from_api = (json.loads(roadster_data)["epoch_jd"])

    orbitURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@10'&MAKE_EPHEM= 'YES'" + \
               "&TABLE_TYPE= 'ELEMENTS'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'&OUT_UNITS= 'AU-D'" + \
               "&REF_PLANE = 'ECLIPTIC' &REF_SYSTEM = 'J2000' &TP_TYPE = 'ABSOLUTE' &ELEM_LABELS = 'YES' &CSV_FORMAT = 'NO' & OBJ_DATA = 'YES'"

    marsDistURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'" + \
                  "&TABLE_TYPE= 'OBSERVER'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'" + \
                  "&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'" + \
                  "&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'" + \
                  "&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'"

    earthDistURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER='500@399'" + \
                    "&MAKE_EPHEM='YES'&TABLE_TYPE='OBSERVER'&START_TIME='"+ NOW + "'&STOP_TIME = '" + TOMORROW + "'"+ \
                    "&STEP_SIZE = '1 d' &CAL_FORMAT = 'CAL' &TIME_DIGITS = 'MINUTES' &ANG_FORMAT = 'HMS' " + \
                    "&OUT_UNITS = 'KM-S' &RANGE_UNITS = 'AU' &APPARENT = 'AIRLESS' &SUPPRESS_RANGE_RATE = 'NO' " + \
                    "&SKIP_DAYLT = 'NO' &EXTRA_PREC = 'NO' &R_T_S_ONLY = 'NO' &REF_SYSTEM = 'J2000' " + \
                    "&CSV_FORMAT = 'NO' &OBJ_DATA = 'YES' &QUANTITIES = '19,20'"


    # Get the data for the Mars Distance information from JPL Horizons API
    fg = makeHTTP(marsDistURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for Mars distance
    writeFile(BASE +'mars', fg, 'w')

    # Get the data for the Orbit Parameters information from JPL Horizons API
    fg = makeHTTP(orbitURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for Orbit Parameters
    writeFile(BASE + 'orbit', fg, 'w')

    # Get the data for the Earth Distance  information from JPL Horizons API
    fg = makeHTTP(earthDistURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for the Earth Distance
    writeFile(BASE + 'earth', fg, 'w')


    # Get EPOCH
    sb = ['roadster_mars0.zsh epoch', 'epoch']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    epoch = float(g.stdout.strip())

    CDATA = CDATA + '{"LCL_epoch":' + str(epoch) + ','
    CDATA = CDATA + '"API_epoch":' + str(epoch_from_api) + ','

    # Distance from Mars
    sb = ['roadster_mars0.zsh marsDistance', 'marsDistance']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    distanceFromMarskm = float(g.stdout.strip()) * float(AU_TO_KM)
    distanceFromMarsmi = float(distanceFromMarskm) * float(KM_TO_MILES)

    CDATA = CDATA + '"API_mars_distance_km":' + str(mars_distance_from_api_km) + ','
    CDATA = CDATA + '"API_mars_distance_mi":' + str(mars_distance_from_api_mi) + ','
    CDATA = CDATA + '"LCL_mars_distance_km":' + str(distanceFromMarskm) + ','
    CDATA = CDATA + '"LCL_mars_distance_mi":' + str(distanceFromMarsmi) + ','

    # Orbital Speed
    sb = ['roadster_mars0.zsh speed','speed']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    OrbitalSpeedkph = float(g.stdout.strip()) * (float(60.0) * float(60.0))
    OrbitalSpeedmph = float(OrbitalSpeedkph) * float(KM_TO_MILES)

    CDATA = CDATA + '"API_speed_kph":' + str(OrbitalSpeedkph) + ','
    CDATA = CDATA + '"API_speed_mph":' + str(OrbitalSpeedmph) + ','
    CDATA = CDATA + '"LCL_speed_kph":' + str(orbital_speed_kph) + ','
    CDATA = CDATA + '"LCL_speed_mph":' + str(orbital_speed_mph) + ','

    CDATA = CDATA + '"LAST": 0}'
    return CDATA

    '''
        Helper functions
    '''


def percentage(percent, whole):
    return (percent * whole) / 100.0


def plus_percent(percent, value):
    return value + percentage(percent, value)


def minus_percent(percent, value):
    return value - percentage(percent, value)
