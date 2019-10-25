"""Launches module

This is a module which allows wrapper access to data about
all SpaceX launches - both past and (as far as is known) in
the future

This file is imported as a module and contains the following
functions:

    * alllaunches - returns all launch information
    * latest - returns information about the latest launches
    * nextlaunch - returns information about the next launch
    * upcoming - returns information about the future launches
    * past - returns information about previous launches
    * one - returns information about a specific launch

"""
from . import urldata
from . import utils


def alllaunches(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all SpaceX launches

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all launch
        events respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)


def latest(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about the latest SpaceX launches

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the latest launch
        events respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return utils.makeRequest(requestUrl, timeOut, parameters)


def nextlaunch(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about the next SpaceX launch

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the next launch
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return utils.makeRequest(requestUrl, timeOut, parameters)


def upcoming(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about future SpaceX launches

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the future launch
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return utils.makeRequest(requestUrl, timeOut, parameters)


def past(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about past SpaceX launches

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of previous launches
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.past_launches
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(launch='', parameters='', timeOut=1):
    """
    :type launch: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific SpaceX launch

    Parameters
    ----------
    launch : launch ID (str)
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of an individual launch
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain + "/" + launch
    return utils.makeRequest(requestUrl, timeOut, parameters)
