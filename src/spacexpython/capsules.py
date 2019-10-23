"""Capsules module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about the capsules within
SpaceX's fleet

This file is imported as a module and contains the following
functions:

    * capsules - returns all capsules
    * upcoming - returns information about upcoming capsules
    * past - returns information about past capsules
    * one - returns information about a specific capsule

"""
from . import urldata
from . import utils


def capsules(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all capsules

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the capsules
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules
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
    a string in JSON format containing details of all the
        upcoming capsules respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_capsules
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
    a string in JSON format containing details of all the
        past capsules respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.past_capsules
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(capsule_id, parameters='', timeOut=1):
    """

    :type capsule_id: [str]
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific capsule

    Parameters
    ----------
    capsule_id : ID of the capsule of interest
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the
        capsule respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + \
        "/" + str(capsule_id)
    return utils.makeRequest(requestUrl, timeOut, parameters)
