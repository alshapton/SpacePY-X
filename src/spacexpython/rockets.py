
"""Rockets module

This is a module which allows wrapper access to the functions within the SpaceX
API to return information about the rockets

This file is imported as a module and contains the following
functions:

    * all - returns all rockets
    * rocket - returns information about one rocket rocket type

    # CONSIDER REMOVING THESE FUNCTIONS
    * falcon1 - returns information about the Falcon 1
    * falcon9 - returns information about the Falcon 9
    * bfr - returns information about the Big Falcon Rocket
    * falconHeavy - returns information about the Falcon Heavy
"""
import urldata
import utils

def all(parameters='',timeOut=1):
    """ Return a JSON document containing ALL rockets

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Returns
    -------
    string
        a JSON document containing a list of rockets
    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets + utils.jsonParameters(parameters)
    print(requestUrl)
    return utils.makeRequest(requestUrl,timeOut)

def rocket(rocket,parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets + "/" + rocket
    return utils.makeRequest(requestUrl,timeOut)

# Consider removing these
def falcon1(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falcon1
    return utils.makeRequest(requestUrl,timeOut)

def falcon9(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falcon9
    return utils.makeRequest(requestUrl,timeOut)

def falconHeavy(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falconheavy
    return utils.makeRequest(requestUrl,timeOut)

def bfr(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.bigfalconrocket
    return utils.makeRequest(requestUrl,timeOut)
