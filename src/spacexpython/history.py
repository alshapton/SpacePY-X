"""History module

This is a module which allows wrapper access to the history of SpaceX;
specifically events which have occurred in the company's timeline

This file is imported as a module and contains the following
functions:

    * history - returns all history information
    * one - returns information about a specific event

"""
from . import urldata
from . import utils


def history(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about the SpaceX timeline

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all historical
        events respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_history
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(event='', parameters='', timeOut=1):
    """
    :type event: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about the SpaceX timeline

    Parameters
    ----------
    event : ID of the event of interest (str)
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of a specific
     historical event respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_history + \
        "/" + event
    return utils.makeRequest(requestUrl, timeOut, parameters)
