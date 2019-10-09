"""Utilities module

This is a utilities module with common functionality which is used by many
other modules.

This file is imported as a module and contains the following
functions:

    * jsonParameters - converts a JSON document into a URL parameter string
    * makeRequest - function to call a REST api
"""
import ast
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


def validateParameters(inParameters,inFunction,subfunction):
    #If there are no parameters, then nothing needs validating.
    if (inParameters == ''):
        return True
    parameters = ast.literal_eval(inParameters)
    # Get the function name from the call
    discard, function = inFunction.split('.')

    # Open the database
    db = TinyDB('matrixDB.json')
    # Get the list of rows for this function/subfunction
    Row = Query()
    subFunctionLine = db.get((Row.function == function) & (Row.subfunction == subfunction))

    functionParameters = subFunctionLine.get("parameters")
    fp=[]
    ft=[]

    cfp=0
    # get list of parameters in function/subfunction and populate 2 lists with their names and types
    for i in functionParameters:
        cfp=cfp+1
        fp.append(i.get("parameter"))
        ft.append(i.get("parameter")+ ".<class '" + i.get("type")+"'>")

    # if there are no parameters applicable for this function, return true
    if (cfp == 0):
        return True

    # Cycle though list of supplied parameters, testing each for name validity and type validity
    for key, value in parameters.items():
        if key not in fp:
            raise SpaceXParameterError(key + " is not a valid parameter for "+ function + "." + subfunction)
        else:

            for g in ft:
                p, t = g.split('.')
                if (p == key):
                    break
                    
            if (t == "<class 'int'>"):
                try:
                    attempt=int(value)
                    break
                except ValueError:
                    raise SpaceXParameterError("Type '" + str(type(value)).replace("<class '", "").replace("'>","") + "' is not valid for " + function + "." + subfunction + "(parameter: " + key + ")")

            if (t == "<class 'bool'>"):
                if (value.upper() not in ['TRUE', 'FALSE']):
                    raise SpaceXParameterError("Type '" + str(type(value)).replace("<class '", "").replace("'>", "") + "' is not valid for " + function + "." + subfunction + "(parameter: " + key + ")")
            else:
                # if the parameter is of the incorrect type then raise an exception
                if (key  + "." + str(type(value))) not in ft:
                    raise SpaceXParameterError("Type '" + str(type(value)).replace("<class '","").replace("'>","") + "' is not valid for " + function + "." + subfunction + "(parameter: "+ key + ")")
    # If every parameter and type combination work out then good to go !
    return True


def func_name():
    # Source: https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
    return currentFuncName(1)
