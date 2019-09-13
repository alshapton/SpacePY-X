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
BASE = 'data/roadster/roadster.'


def test_name(setup_module):
    assert json.loads(setup_module)["API_name"] == "Elon Musk\'s Tesla Roadster"

    
def test_launch_date_utc(setup_module):
    assert json.loads(setup_module)["API_launch_date_utc"] == "2018-02-06T20:45:00.000Z"

    
def test_launch_date_unix(setup_module):
    assert json.loads(setup_module)["API_launch_date_unix"] == 1517949900

    
def test_launch_mass_kg(setup_module):
    assert json.loads(setup_module)["API_launch_mass_kg"] == 1350

    
def test_launch_mass_lbs(setup_module):
    assert json.loads(setup_module)["API_launch_mass_lbs"] == 2976

    
def test_norad_id(setup_module):
    assert json.loads(setup_module)["API_norad_id"] == 43205

    
def test_orbit_type(setup_module):
    assert json.loads(setup_module)["API_orbit_type"] == "heliocentric"

    
def test_wikipedia(setup_module):
    assert json.loads(setup_module)["API_wikipedia"] == "https://en.wikipedia.org/wiki/Elon_Musk%27s_Tesla_Roadster"
    
    
def test_details(setup_module):
    assert json.loads(setup_module)["API_details"] == "Elon Musk's Tesla Roadster is an electric " + \
        "sports car that served as the dummy payload for the February 2018 Falcon Heavy test flight " + \
        "and is now an artificial satellite of the Sun. Starman, a mannequin dressed in a spacesuit, " + \
        "occupies the driver's seat. The car and rocket are products of Tesla and SpaceX. This 2008-model " + \
        "Roadster was previously used by Musk for commuting, and is the only consumer car sent into space."

    
def test_mars_distance_km(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"]) <= \
        json.loads(setup_module)["API_mars_distance_km"] <= \
        plus_percent(1, json.loads(setup_module)["LCL_mars_distance_km"])

    
def test_mars_distance_mi(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"]) <= \
        json.loads(setup_module)["API_mars_distance_mi"] <= \
        plus_percent(1, json.loads(setup_module)["LCL_mars_distance_mi"])

    
def test_earth_distance_km(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_earth_distance_km"]) <= json.loads(setup_module)[
        "API_earth_distance_km"] <= plus_percent(1, json.loads(setup_module)["LCL_earth_distance_km"])

    
def test_earth_distance_mi(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_earth_distance_mi"]) <= json.loads(setup_module)[
        "API_earth_distance_mi"] <= plus_percent(1, json.loads(setup_module)["LCL_earth_distance_mi"])

    
def test_orbital_speed_kph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_kph"]) <= json.loads(setup_module)[
        "API_speed_kph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_kph"])

    
def test_orbital_speed_mph(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_speed_mph"]) <= json.loads(setup_module)[
        "API_speed_mph"] <= plus_percent(1, json.loads(setup_module)["LCL_speed_mph"])

    
def test_epoch(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_epoch"]) <= json.loads(setup_module)[
        "API_epoch"] <= plus_percent(1, json.loads(setup_module)["LCL_epoch"])

    
def test_sma(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_sma"]) <= json.loads(setup_module)[
        "API_sma"] <= plus_percent(1, json.loads(setup_module)["LCL_sma"])

    
def test_ec(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_ec"]) <= json.loads(setup_module)[
        "API_ec"] <= plus_percent(1, json.loads(setup_module)["LCL_ec"])

    
def test_qr(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_qr"]) <= json.loads(setup_module)[
        "API_qr"] <= plus_percent(1, json.loads(setup_module)["LCL_qr"])

    
def test_ad(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_ad"]) <= json.loads(setup_module)[
        "API_ad"] <= plus_percent(1, json.loads(setup_module)["LCL_ad"])

    
def test_om(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_om"]) <= json.loads(setup_module)[
        "API_om"] <= plus_percent(1, json.loads(setup_module)["LCL_om"])

    
def test_w(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_w"]) <= json.loads(setup_module)[
        "API_w"] <= plus_percent(1, json.loads(setup_module)["LCL_w"])

    
def test_inc(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_inc"]) <= json.loads(setup_module)[
        "API_inc"] <= plus_percent(1, json.loads(setup_module)["LCL_inc"])

    
def test_period(setup_module):
    assert minus_percent(1, json.loads(setup_module)["LCL_period"]) <= json.loads(setup_module)[
        "API_period"] <= plus_percent(1, json.loads(setup_module)["LCL_period"])


@pytest.fixture(scope='module')
def setup_module():
    CDATA = ""
    roadster_data=''
    try:
        roadster_data = alphaOrder(spacexpython.roadster.roadster())
    except spacexpython.utils.SpaceXReadTimeOut:
        pytest.xfail("Space/X API Read Timed Out")
        print("Failure on info.roadster")

    CDATA = CDATA + '{"API_name":"' + (json.loads(roadster_data)["name"]) + '",'
    
    CDATA = CDATA + '"API_launch_date_utc":"' + str((json.loads(roadster_data)["launch_date_utc"])) + '",'
    CDATA = CDATA + '"API_launch_date_unix":' + str((json.loads(roadster_data)["launch_date_unix"])) + ','
    CDATA = CDATA + '"API_launch_mass_kg":' + str((json.loads(roadster_data)["launch_mass_kg"])) + ','
    
    CDATA = CDATA + '"API_launch_mass_lbs":' + str((json.loads(roadster_data)["launch_mass_lbs"])) + ','
    CDATA = CDATA + '"API_norad_id":' + str((json.loads(roadster_data)["norad_id"])) + ','
    CDATA = CDATA + '"API_orbit_type":"' + str((json.loads(roadster_data)["orbit_type"])) + '",'
    CDATA = CDATA + '"API_wikipedia":"' + str((json.loads(roadster_data)["wikipedia"])) + '",'
    CDATA = CDATA + '"API_details":"' + str((json.loads(roadster_data)["details"])) + '",'

    mars_distance_from_api_km = (json.loads(roadster_data)["mars_distance_km"])
    mars_distance_from_api_mi = (json.loads(roadster_data)["mars_distance_mi"])
    earth_distance_from_api_km = (json.loads(roadster_data)["earth_distance_km"])
    earth_distance_from_api_mi = (json.loads(roadster_data)["earth_distance_mi"])

    orbital_speed_kph = (json.loads(roadster_data)["speed_kph"])
    orbital_speed_mph = (json.loads(roadster_data)["speed_mph"])

    epoch_from_api = (json.loads(roadster_data)["epoch_jd"])
    sma_from_api = (json.loads(roadster_data)["semi_major_axis_au"])
    ec_from_api = (json.loads(roadster_data)["eccentricity"])
    qr_from_api = (json.loads(roadster_data)["periapsis_au"])
    ad_from_api = (json.loads(roadster_data)["apoapsis_au"])
    om_from_api = (json.loads(roadster_data)["longitude"])
    w_from_api = (json.loads(roadster_data)["periapsis_arg"])
    inc_from_api = (json.loads(roadster_data)["inclination"])
    period_from_api = (json.loads(roadster_data)["period_days"])

    orbitURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@10'&MAKE_EPHEM= 'YES'" + \
               "&TABLE_TYPE= 'ELEMENTS'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'&OUT_UNITS= 'AU-D'" + \
               "&REF_PLANE = 'ECLIPTIC' &REF_SYSTEM = 'J2000' &TP_TYPE = 'ABSOLUTE' &ELEM_LABELS = 'YES' &CSV_FORMAT = 'NO' & OBJ_DATA = 'YES'"

    marsDistURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER= '500@499'&MAKE_EPHEM= 'YES'" + \
                  "&TABLE_TYPE= 'OBSERVER'&START_TIME= '" + NOW + "'&STOP_TIME= '" + TOMORROW + "'&STEP_SIZE= '1 d'" + \
                  "&CAL_FORMAT= 'CAL'&TIME_DIGITS= 'MINUTES'&ANG_FORMAT= 'HMS'&OUT_UNITS= 'KM-S'&RANGE_UNITS= 'AU'" + \
                  "&APPARENT= 'AIRLESS'&SUPPRESS_RANGE_RATE= 'NO'&SKIP_DAYLT= 'NO'&EXTRA_PREC= 'NO'&R_T_S_ONLY= 'NO'" + \
                  "&REF_SYSTEM= 'J2000'&CSV_FORMAT= 'NO'&OBJ_DATA= 'YES'&QUANTITIES= '19,20,22'"

    earthDistURL = "https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&COMMAND='-143205'&CENTER='500@399'" + \
                    "&MAKE_EPHEM='YES'&TABLE_TYPE='OBSERVER'&START_TIME='"+ NOW + "'&STOP_TIME = '" + TOMORROW + "'" + \
                    "&STEP_SIZE = '1 d' &CAL_FORMAT = 'CAL' &TIME_DIGITS = 'MINUTES' &ANG_FORMAT = 'HMS' " + \
                    "&OUT_UNITS = 'KM-S' &RANGE_UNITS = 'AU' &APPARENT = 'AIRLESS' &SUPPRESS_RANGE_RATE = 'NO' " + \
                    "&SKIP_DAYLT = 'NO' &EXTRA_PREC = 'NO' &R_T_S_ONLY = 'NO' &REF_SYSTEM = 'J2000' " + \
                    "&CSV_FORMAT = 'NO' &OBJ_DATA = 'YES' &QUANTITIES = '19,20'"

    # Get the data for the Mars Distance information from JPL Horizons API
    fg = makeHTTP(marsDistURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for Mars distance
    writeFile(BASE + 'mars', fg, 'w')

    # Get the data for the Orbit Parameters information from JPL Horizons API
    fg = makeHTTP(orbitURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for Orbit Parameters
    writeFile(BASE + 'orbit', fg, 'w')

    # Get the data for the Earth Distance  information from JPL Horizons API
    fg = makeHTTP(earthDistURL, 1)
    # Create a new file with the results of the call to the JPL Horizons API for the Earth Distance
    writeFile(BASE + 'earth', fg, 'w')

    # EPOCH
    sb = ['./script_roadster.zsh epoch', 'epoch']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    epoch = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_epoch":' + str(epoch) + ','
    CDATA = CDATA + '"API_epoch":' + str(epoch_from_api) + ','

    # Semi-major Axis
    sb = ['./script_roadster.zsh sma', 'sma']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    sma = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_sma":' + str(sma) + ','
    CDATA = CDATA + '"API_sma":' + str(sma_from_api) + ','

    # Eccentricity
    sb = ['./script_roadster.zsh ec', 'ec']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    ec = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_ec":' + str(ec) + ','
    CDATA = CDATA + '"API_ec":' + str(ec_from_api) + ','

    # Periapsis
    sb = ['./script_roadster.zsh qr', 'qr']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    qr = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_qr":' + str(qr) + ','
    CDATA = CDATA + '"API_qr":' + str(qr_from_api) + ','

    # Apoapsis
    sb = ['./script_roadster.zsh ad', 'ad']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    ad = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_ad":' + str(ad) + ','
    CDATA = CDATA + '"API_ad":' + str(ad_from_api) + ','

    # Longitude
    sb = ['./script_roadster.zsh om', 'om']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    om = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_om":' + str(om) + ','
    CDATA = CDATA + '"API_om":' + str(om_from_api) + ','

    # Longitude
    sb = ['./script_roadster.zsh w', 'w']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    w = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_w":' + str(w) + ','
    CDATA = CDATA + '"API_w":' + str(w_from_api) + ','

    # Apoapsis
    sb = ['./script_roadster.zsh inc', 'inc']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    inc = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_inc":' + str(inc) + ','
    CDATA = CDATA + '"API_inc":' + str(inc_from_api) + ','

    # Period (days)
    sb = ['./script_roadster.zsh period', 'period']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    period = float(g.stdout.strip())

    CDATA = CDATA + '"LCL_period":' + str(period) + ','
    CDATA = CDATA + '"API_period":' + str(period_from_api) + ','

    # Distance from Earth
    sb = ['./script_roadster.zsh earthDistance', 'earthDistance']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    distanceFromEarthkm = float(g.stdout.strip()) * float(AU_TO_KM)
    distanceFromEarthmi = float(distanceFromEarthkm) * float(KM_TO_MILES)

    CDATA = CDATA + '"API_earth_distance_km":' + str(earth_distance_from_api_km) + ','
    CDATA = CDATA + '"API_earth_distance_mi":' + str(earth_distance_from_api_mi) + ','
    CDATA = CDATA + '"LCL_earth_distance_km":' + str(distanceFromEarthkm) + ','
    CDATA = CDATA + '"LCL_earth_distance_mi":' + str(distanceFromEarthmi) + ','

    # Distance from Mars
    sb = ['./script_roadster.zsh marsDistance', 'marsDistance']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    distanceFromMarskm = float(g.stdout.strip()) * float(AU_TO_KM)
    distanceFromMarsmi = float(distanceFromMarskm) * float(KM_TO_MILES)

    CDATA = CDATA + '"API_mars_distance_km":' + str(mars_distance_from_api_km) + ','
    CDATA = CDATA + '"API_mars_distance_mi":' + str(mars_distance_from_api_mi) + ','
    CDATA = CDATA + '"LCL_mars_distance_km":' + str(distanceFromMarskm) + ','
    CDATA = CDATA + '"LCL_mars_distance_mi":' + str(distanceFromMarsmi) + ','

    # Orbital Speed
    sb = ['./script_roadster.zsh speed', 'speed']
    g = subprocess.run(sb, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    OrbitalSpeedkph = float(g.stdout.strip()) * (float(60.0) * float(60.0))
    OrbitalSpeedmph = float(OrbitalSpeedkph) * float(KM_TO_MILES)

    CDATA = CDATA + '"API_speed_kph":' + str(OrbitalSpeedkph) + ','
    CDATA = CDATA + '"API_speed_mph":' + str(OrbitalSpeedmph) + ','
    CDATA = CDATA + '"LCL_speed_kph":' + str(orbital_speed_kph) + ','
    CDATA = CDATA + '"LCL_speed_mph":' + str(orbital_speed_mph) + ','

    CDATA = CDATA + '"LAST": 0}'

    return CDATA



