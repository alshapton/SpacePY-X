"""Crew module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about the astronauts on SpaceX
missions

This file is imported as a module and contains the following
functions:

    * crew - returns all crew information

"""
from . import urldata
from . import utils


def crew(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Returns details about all crew craft

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing an optional list
        of filters
    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of all the crews
        respecting any filters
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_crew
    return utils.makeRequest(requestUrl, timeOut)
