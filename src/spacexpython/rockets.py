
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
    * falconheavy - returns information about the Falcon Heavy
"""
from . import urldata
from . import utils

def allrockets(parameters='',timeOut=1):
    """ Return a JSON document containing ALL rockets

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    requestURL : str
        string to pass into the REST API
    timeOut : int
        optional - API call timeout
    parameters : str
        optional parameters to append to URL as query modifiers

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing a list of rockets
    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    return utils.makeRequest(requestUrl,timeOut,parameters)

def rocket(rocket,parameters='',timeOut=1):
    """ Return a JSON document containing details of a specific rocket

    :type rocket: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    rocket
        mandatory - the rocket ID of the rocket in question
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing a single rocket
    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets + "/" + rocket
    return utils.makeRequest(requestUrl,timeOut)


def falcon1(parameters='',timeOut=1):
    """ Return a JSON document containing details of a the Falcon 1 rocket

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing details about the Falcon 1 rocket
    """
    requestUrl = urldata.Domain.main + urldata.Domain.falcon1
    return utils.makeRequest(requestUrl,timeOut,parameters)

def falcon9(parameters='',timeOut=1):
    """ Return a JSON document containing details of a the Falcon 9 rocket

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing details about the Falcon 9 rocket
    """
    requestUrl = urldata.Domain.main + urldata.Domain.falcon9
    return utils.makeRequest(requestUrl,timeOut,parameters)

def falconheavy(parameters='',timeOut=1):
    """ Return a JSON document containing details of a the Falcon Heavy rocket

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing details about the Falcon Heavy rocket
    """
    requestUrl = urldata.Domain.main + urldata.Domain.falconheavy
    return utils.makeRequest(requestUrl,timeOut,parameters)

def bfr(parameters='',timeOut=1):
    """ Return a JSON document containing details of a the Big Falcon Rocket

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing details about the Big Falcon Rocket
    """
    requestUrl = urldata.Domain.main + urldata.Domain.bigfalconrocket
    return utils.makeRequest(requestUrl,timeOut,parameters)

def starship(parameters='',timeOut=1):
    """ Return a JSON document containing details of a the Starship

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds of the REST api call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit

    Returns
    -------
    string
        a JSON document containing details about the Starship
    """
    requestUrl = urldata.Domain.main + urldata.Domain.starship
    return utils.makeRequest(requestUrl,timeOut,parameters)
