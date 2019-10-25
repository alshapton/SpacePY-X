"""Payload module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about payloads SpaceX has carried

This file is imported as a module and contains the following
functions:

    * payloads - returns all payload information
    * one - returns information about a specific payload

"""
from . import urldata
from . import utils


def payloads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about payloads SpaceX has carried

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all payloads
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_payloads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)


def one(payload='', parameters='', timeOut=1):
    """
    :type payload : [str]
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about an individual payload SpaceX has carried

    Parameters
    ----------
    payload : Payload idnentifier (str)
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of a single payload
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_payloads + "/" + payload
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)
