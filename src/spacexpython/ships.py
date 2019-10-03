from . import urldata
from . import utils


def ships(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_ships
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(ship='', parameters='', timeOut=1):
    """

    :type ship: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_ships + "/" + ship
    return utils.makeRequest(requestUrl, timeOut, parameters)
