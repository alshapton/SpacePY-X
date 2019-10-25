"""Landingpads module

This is a module which allows wrapper access to information concerning
the landing pads that SpaceX uses to allow its' rocket cores to land
ready for refurbishment and reuse. Note that this does NOT include
drone ships

This file is imported as a module and contains the following
functions:

    * landingpads - returns all landing pad information
    * one - returns information about a specific pad

"""
from . import urldata
from . import utils


def landingpads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about the SpaceX landing pads

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all landing pads
        used by SpaceX respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_landingpads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)


def one(pad='', parameters='', timeOut=1):
    """
    :type pad: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific SpaceX landing pad

    Parameters
    ----------
    pad: landing pad of interest (str)
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of a single landing pad
        used by SpaceX respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + \
            urldata.Domain.main_landingpads + "/" + pad
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)
