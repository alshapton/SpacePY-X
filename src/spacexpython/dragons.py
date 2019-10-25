"""Dragons module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about the dragon craft

This file is imported as a module and contains the following
functions:

    * dragon - returns all dragon information
    * one - returns information about a specific dragon craft

"""
from . import urldata
from . import utils


def dragons(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all dragon craft

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the dragon craft
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_dragons
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(dragon='', parameters='', timeOut=1):
    """

    :type dragon: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about a specific dragon craft

    Parameters
    ----------
    dragon : name of the dragon craft of interest
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the dragon craft
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_dragons + \
        "/" + dragon
    return utils.makeRequest(requestUrl, timeOut, parameters)
