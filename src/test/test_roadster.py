
import sys

sys.path.append('../')
import pytest

import spacexpython
from spacexpython.exceptions import *
from spacexpython.utils import *
from .tutils import *
import subprocess
from time import gmtime, strftime
from datetime import timedelta,datetime


# Conversion factors:
# Kilometers to Miles
# Astronomical Units to Kilometres
KM_TO_MILES = 0.621371
AU_TO_KM = 149598073.0

NOW=strftime("%Y-%m-%d %H:%M:%S", gmtime())
END=datetime.now()+ timedelta(days=1)
TOMORROW=END.strftime('%Y-%m-%d %H:%M:%S')


def test_mars_distance_km(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"]) <= json.loads(setup_module)["API_mars_distance_km"] <= plus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"])

def test_mars_distance_mi(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"]) <= json.loads(setup_module)["API_mars_distance_mi"] <= plus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"])

def test_orbital_speed_kph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_kph"]) <= json.loads(setup_module)["API_speed_kph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_kph"])

def test_orbital_speed_mph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_mph"]) <= json.loads(setup_module)["API_speed_mph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_mph"])



@pytest.fixture(scope='module')
def setup_module():
    CDATA = ""

    try:
        roadster_data = alphaOrder(spacexpython.roadster.roadster())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.roadster")

    mars_distance_from_api_km=(json.loads(roadster_data)["mars_distance_km"])
    mars_distance_from_api_mi=(json.loads(roadster_data)["mars_distance_mi"])

    orbital_speed_kph = (json.loads(roadster_data)["speed_kph"])
    orbital_speed_mph = (json.loads(roadster_data)["speed_mph"])

    mars = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'" + \
           "&TABLE_TYPE= 'OBSERVER'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'" + \
           "&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'" + \
           "&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'" + \
           "&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'"

    fg = makeHTTP(mars, 1)

    # Create a new file with the results of the call to the JPL Horizons API for Mars distance
    writeFile('data/roadster/roadster.mars',fg,'w')

    # Distance from Mars
    sb="('roadster_mars1.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    distanceFromMarskm=float(g.stdout.strip() ) * float(AU_TO_KM)
    distanceFromMarsmi = float(distanceFromMarskm) * float(KM_TO_MILES)

    CDATA=CDATA +'{"API_mars_distance_km":'+ str(mars_distance_from_api_km) + ','
    CDATA=CDATA+ '"API_mars_distance_mi":'+ str(mars_distance_from_api_mi) + ','
    CDATA=CDATA +'"LCL_mars_distance_km":'+ str(distanceFromMarskm) + ','
    CDATA=CDATA+ '"LCL_mars_distance_mi":'+ str(distanceFromMarsmi) + ','

    # Orbital Speed
    sb="('roadster_mars2.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    OrbitalSpeedkph=float(g.stdout.strip() ) * (float(60.0) * float(60.0))
    OrbitalSpeedmph = float(OrbitalSpeedkph) * float(KM_TO_MILES)

    CDATA=CDATA +'"API_speed_kph":'+ str(OrbitalSpeedkph) + ','
    CDATA=CDATA+ '"API_speed_mph":'+ str(OrbitalSpeedmph) + ','
    CDATA=CDATA +'"LCL_speed_kph":'+ str(orbital_speed_kph) + ','
    CDATA=CDATA+ '"LCL_speed_mph":'+ str(orbital_speed_mph) + ','

    CDATA=CDATA + '"LAST": 0}'
    return CDATA


    '''
        Helper functions
    '''
def percentage(percent, whole):
  return (percent * whole) / 100.0

def plus_percent(percent,value):
    return value + percentage(percent,value)

def minus_percent(percent,value):
    return value - percentage(percent,value)


