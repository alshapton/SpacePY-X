"""Roadster module

This is a module which allows wrapper access to information about Elon
Musk's Tesla Model 3 Roadster which is now an artificial satellite of
the Sun.

This file is imported as a module and contains the following
function:

    * roadster - returns all roadster information

"""
from . import urldata
from . import utils


def roadster(timeOut=1):
    """

    :type timeOut: Optional[int]

    Returns details about the Tesla Model 3 Roadster

    Parameters
    ----------

    timeOut : time out in seconds

    Returns
    -------
    a string in JSON format containing details of the Tesla Model 3
        Roadster, including position, speed etc
    """
    utils.validateParameters('', __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_roadster
    return utils.makeRequest(requestUrl, timeOut)
