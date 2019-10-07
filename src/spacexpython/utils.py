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

from tinydb import TinyDB, Query


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


def validateParameters(parameters,function,subfunction):
    # Open the database
    db = TinyDB('matrix.json')
    # Get the list of rows for this function/subfunction
    Row = Query()
    subFunctionLine = db.get((Row.function == function) & (Row.subfunction == subfunction))
    print(subFunctionLine)
    functionParameters = subFunctionLine.get("parameters")
    fp=[]
    ft=[]

    # get list of parameters in function/subfunction and populate 2 lists with their names and types
    for i in functionParameters:
        fp.append(i.get("parameter"))
        ft.append(i.get("parameter")+ ".<type '" + i.get("type")+"'>")

    # Cycle though list of supplied parameters, testing each for name validity and type validity
    for i in parameters:
        if i not in fp:
            raise SpaceXParameterError(i + " is not a valid parameter for "+ function + "." + subfunction)
        else:
            if (i + "." + str(type(parameters[i]))) not in ft:
                raise SpaceXParameterError(str(type(parameters[i])) + " is not valid for " + function + "." + subfunction + "(parameter: "+ i + ")")
    # If every parameter and type combination work out then good to go !
    return True