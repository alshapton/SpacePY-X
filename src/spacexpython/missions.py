"""Missions module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about SpaceX missions

This file is imported as a module and contains the following
functions:

    * missions - returns all mission information
    * one - returns information about a specific mission

"""
from . import urldata
from . import utils


def missions(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all missions

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all missions
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_missions
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)


def one(mission='', parameters='', timeOut=1):

    """
    :type mission: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific mission

    Parameters
    ----------
    mission : Mission identifier (str)
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of a single mission
        respecting any filters
    """

    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_missions + "/" + mission
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)
