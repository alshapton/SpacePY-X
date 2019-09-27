
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
from . import urldata
from . import utils

def allrockets(parameters='',timeOut=1):
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
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    return utils.makeRequest(requestUrl,timeOut,parameters)

def rocket(rocket,parameters='',timeOut=1):
    """ Return a JSON document containing details of a specific rocket

    Parameters
    ----------
    rocket
        mandatory - the rocket ID of the rocket in question
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Returns
    -------
    string
        a JSON document containing a list of rockets
    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets + "/" + rocket
    return utils.makeRequest(requestUrl,timeOut)


def falcon1(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falcon1
    return utils.makeRequest(requestUrl,timeOut,parameters)

def falcon9(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falcon9
    return utils.makeRequest(requestUrl,timeOut,parameters)

def falconHeavy(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.falconheavy
    return utils.makeRequest(requestUrl,timeOut,parameters)

def bfr(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.bigfalconrocket
    return utils.makeRequest(requestUrl,timeOut,parameters)
