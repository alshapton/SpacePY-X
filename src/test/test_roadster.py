
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

distanceFromMarskm = 0
mars_distance_from_api = 0

@pytest.fixture(scope='module')
def setup():

    try:
        roadster_data = alphaOrder(spacexpython.roadster.roadster())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.roadster")


    mars = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'" + \
           "&TABLE_TYPE= 'OBSERVER'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'" + \
           "&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'" + \
           "&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'" + \
           "&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'"

    fg = makeHTTP(mars, 1)

    # Distance from Mars
    sb="('roadster_mars1.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    print (g.stdout)
    distanceFromMarskm=float(g.stdout.strip() ) * float(AU_TO_KM)
    distanceFromMarsmi = float(distanceFromMarskm) * float(KM_TO_MILES)

    # Orbital Speed
    sb="('roadster_mars2.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    OrbitalSpeedkm=float(g.stdout.strip() ) * (float(60.0) * float(60.0))
    OrbitalSpeedmi = float(OrbitalSpeedkm) * float(KM_TO_MILES)

def test_mars_distance():
    assert mars_distance_from_api >= minus_percent(1,distanceFromMarskm) and distanceFromMarskm <= plus_percent(1,distanceFromMarskm)

def test_roadster():
    roadster_data=''

    mars="https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'" + \
    "&TABLE_TYPE= 'OBSERVER'&START_TIME= '"+ NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'" + \
    "&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'"  + \
    "&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'" + \
    "&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'"

    fg=makeHTTP(mars, 1)

    writeFile('roadster.output',fg)

    # Distance from Mars
    sb="('roadster_mars1.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    print (g.stdout)
    distanceFromMarskm=float(g.stdout.strip() ) * float(149598073.0)
    distanceFromMarsmi = float(distanceFromMarskm) * float(KM_TO_MILES)

    # Orbital Speed
    sb="('roadster_mars2.zsh')"
    g=subprocess.run(sb,stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    OrbitalSpeedkm=float(g.stdout.strip() ) * float(60.0) * float(60.0)
    OrbitalSpeedmi = float(OrbitalSpeedkm) * float(KM_TO_MILES)

    print(distanceFromMarskm)


    roadster_result=alphaOrder(readJSONFile('roadster/roadster.json'))
    #print(roadster_result)
    try:
        roadster_data = alphaOrder(spacexpython.roadster.roadster())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print ("Failure on info.roadster")
    print (roadster_data)
    #writeJSONFile('roadster/roadster.json',roadster_data)
    #assert roadster_result == roadster_data
    mars_distance_from_api=(json.loads(roadster_data)["mars_distance_km"])
    assert distanceFromMarskm >= minus_percent(1,distanceFromMarskm) and distanceFromMarskm <= plus_percent(1,distanceFromMarskm)
    print (minus_percent(0.5,distanceFromMarskm))
    print (mars_distance_from_api)
    print (plus_percent(0.5,distanceFromMarskm))


def percentage(percent, whole):
  return (percent * whole) / 100.0

def plus_percent(percent,value):
    return value + percentage(percent,value)

def minus_percent(percent,value):
    return value - percentage(percent,value)
#https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND= '-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'&TABLE_TYPE= 'OBSERVER'&START_TIME= '2019-08-26 01:01:01'&STOP_TIME= '2019-08-27 01:01:01'&STEP_SIZE= '1 d'&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'


