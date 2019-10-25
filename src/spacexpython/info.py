"""Info module

This is a module which allows wrapper access to the technical detail
of SpaceX, together with information about the API and applications
using it

This file is imported as a module and contains the following
functions:

    * company - returns company information
    * api - returns information the API version and endpoints etc
    * clients - returns information regarding clients (wrappers)
    * apps - returns applications using the SpaceX API

"""
from . import urldata
from . import utils


def company(timeOut=1):
    """

    :type timeOut: Optional[int]

     Returns details about the SpaceX company

    Parameter
    ----------
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the SpaceX company

    """
    utils.validateParameters('', __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_info
    return utils.makeRequest(requestUrl, timeOut)


def api(timeOut=1):
    """

    :type timeOut: Optional[int]

     Returns details about the SpaceX API

    Parameter
    ----------
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the SpaceX API

    """
    utils.validateParameters('', __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_api
    return utils.makeRequest(requestUrl, timeOut)


def clients(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about clients (wrappers) using the SpaceX API

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all clients
        respecting any filters
    """
    utils.validateParameters('', __name__, utils.func_name())
    return utils.getAPISupporting("clients", parameters, timeOut)


def apps(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about applications using the SpaceX API

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all applications
        respecting any filters
    """
    utils.validateParameters('', __name__, utils.func_name())
    return utils.getAPISupporting("apps", parameters, timeOut)
