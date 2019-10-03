"""Utilities module

This is a utilities module with common functionality which is used by many
other modules.

This file is imported as a module and contains the following
functions:

    * jsonParameters - converts a JSON document into a URL parameter string
    * makeRequest - function to call a REST api
"""

import json
import sys

import requests

sys.path.append('../')

from .exceptions import *

def jsonParameters(parameters):
    """

    :type parameters: str

    converts a JSON document into a URL parameter string

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing the list of parameters to add to the `API call`

    Returns
    -------
    parms
        a string which can be appended to the URL
    """
    if (parameters == ''):
        return ''
    else:
        jsonObject=json.loads(parameters)
        parms='?'
        for key in jsonObject:
            value=jsonObject[key]
            parms=parms+key+'='+value+'&'
        return parms[:-1]

def makeRequest(requestUrl, timeOut = 1, parameters = ''):
    """
    :param requestUrl: str
    :param timeOut: Optional[str]
    :param parameters: Optional[str]
    :return: object:

    Sends a request to the API

    Parameters
    ----------
    requestURL : str
        string to pass into the REST API
    timeOut : int
        optional - API call timeout
    parameters : str
        optional parameters to append to URL as query modifiers

    Returns
    -------
    response
        a string which is a JSON document returned from the API

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit
    """

    try:
        url_response = requests.get(url=str(requestUrl)+jsonParameters(parameters), timeout=timeOut)
    except requests.exceptions.ReadTimeout:
        raise SpaceXReadTimeOut('Space/X Timeout Error')
    else:
        response = url_response.json()
    return response
