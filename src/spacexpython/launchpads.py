"""Launchpads module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about the launchpads that
SpaceX use

This file is imported as a module and contains the following
functions:

    * launchpads - returns all launchpad information
    * one - returns information about a specific launchpad

"""

from . import urldata
from . import utils


def launchpads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all launchpads

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the launchpads
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_launchpads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)


def one(pad='', parameters='', timeOut=1):
    """

    :type pad: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific launchpad

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the launchpads
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_launchpads + "/" + pad
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)
