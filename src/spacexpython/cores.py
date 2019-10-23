"""Cores module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about the cores

This file is imported as a module and contains the following
functions:

    * cores - returns all cores
    * upcoming - returns information about upcoming cores
    * past - returns information about past cores
    * one - returns information about a specific core

"""
from . import urldata
from . import utils


def cores(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all cores

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the cores
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_cores
    return utils.makeRequest(requestUrl, timeOut, parameters)


def upcoming(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about upcoming capsules

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of upcoming capsules
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_cores
    return utils.makeRequest(requestUrl, timeOut, parameters)


def past(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about past capsules

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the past capsules
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.past_cores
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(core_serial, parameters='', timeOut=1):
    """

    :type core_serial: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific core

    Parameters
    ----------
    core_serial : Serial number of the core of interest
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of a specific core
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_cores + \
        "/" + str(core_serial)
    return utils.makeRequest(requestUrl, timeOut, parameters)
