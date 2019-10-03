"""Cores module

This is a module which allows wrapper access to the functions within the SpaceX
API to return information about the cores

This file is imported as a module and contains the following
functions:

    * cores - returns all cores
    * upcoming - returns information about upcoming cores
    * past - returns information about past cores
    * one - returns information about a specific core

"""
from . import urldata
from . import utils

def cores(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_cores
    return utils.makeRequest(requestUrl,timeOut,parameters)

def upcoming(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_cores
    return utils.makeRequest(requestUrl,timeOut,parameters)

def past(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.past_cores
    return utils.makeRequest(requestUrl,timeOut,parameters)

def one(core_serial,parameters='',timeOut=1):
    """

    :type core_serial: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_cores + "/" + str(core_serial)
    return utils.makeRequest(requestUrl,timeOut,parameters)
