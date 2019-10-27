"""Ships module

This is a module which allows wrapper access to the functions within
the SpaceX API to return information about SpaceX fleet of ships.
This includes support and recovery vessels as well as the drone ships

This file is imported as a module and contains the following
functions:

    * ships - returns all ship information
    * one - returns information about a specific ship

"""
from . import urldata
from . import utils


def ships(parameters='', timeOut=1):
    """
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about all ships
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_ships
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(ship='', parameters='', timeOut=1):
    """
    :type ship: [str]
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    ship
        the idenfier of the ship of interest
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about a specific ship
    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    requestUrl = urldata.Domain.main \
        + urldata.Domain.main_ships + "/" + ship
    return utils.makeRequest(requestUrl, timeOut, parameters)


def ocisly(parameters='', timeOut=1):
    """
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about the
        "Of Course I still Love You" ship
    """
    utils.validateParameters(parameters, __name__, 'one')
    requestUrl = urldata.Domain.main \
        + urldata.Domain.main_ships + "/" + 'OCISLY'
    return utils.makeRequest(requestUrl, timeOut, parameters)


def jrti1(parameters='', timeOut=1):
    """
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about the
        "Just Read The Instructions" (first iteration) ship
    """
    utils.validateParameters(parameters, __name__, 'one')
    requestUrl = urldata.Domain.main \
        + urldata.Domain.main_ships + "/" + 'JRTI-1'
    return utils.makeRequest(requestUrl, timeOut, parameters)


def jrti2(parameters='', timeOut=1):
    """
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about the
        "Just Read The Instructions" (second iteration) ship
    """
    utils.validateParameters(parameters, __name__, 'one')
    requestUrl = urldata.Domain.main \
        + urldata.Domain.main_ships + "/" + 'JRTI-2'
    return utils.makeRequest(requestUrl, timeOut, parameters)


def asog(parameters='', timeOut=1):
    """
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    Parameters
    ----------
    parameters
        optional - a JSON document containing valid query modifiers
    timeOut
        optional - an integer stating the timeout in seconds
                    of the REST api call

    Returns
    -------
    string
        a JSON document containing details about the
        "A Shortfall Of Gravitas"  ship
    """
    utils.validateParameters(parameters, __name__, 'one')
    requestUrl = urldata.Domain.main \
        + urldata.Domain.main_ships + "/" + 'ASOG'
    return utils.makeRequest(requestUrl, timeOut, parameters)
