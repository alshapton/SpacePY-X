
"""Rockets module

This is a module which allows wrapper access to the functions within the SpaceX
API to return information about the rockets

This file is imported as a module and contains the following
functions:

    * all - returns all rockets
    * rocket - returns information about one rocket rocket type
    * falcon1 - returns information about the Falcon 1
    * falcon9 - returns information about the Falcon 9
    * bfr - returns information about the Big Falcon Rocket
    * falconHeavy - returns information about the Falcon Heavy
"""
import requests
import urldata
import utils

def all():
    """ Return a JSON document containing ALL rockets

    Parameters
    ----------
    None

    Returns
    -------
    string
        a JSON document containing a list of rockets
    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    return utils.makeRequest(requestUrl)

def rocket(rocket):
    # do a case statement here to call other functions, but have those available too.
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets + "/" + rocket
    return utils.makeRequest(requestUrl)

def falcon1():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon1
    return utils.makeRequest(requestUrl)

def falcon9():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon9
    return utils.makeRequest(requestUrl)

def falconHeavy():
    requestUrl = urldata.Domain.main + urldata.Domain.falconheavy
    return utils.makeRequest(requestUrl)

def bfr():
    requestUrl = urldata.Domain.main + urldata.Domain.bigfalconrocket
    return utils.makeRequest(requestUrl)
