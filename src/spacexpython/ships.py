from . import urldata
from . import utils


def ships(parameters='', timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_ships
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(ship='', parameters='', timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_ships + "/" + ship
    return utils.makeRequest(requestUrl, timeOut, parameters)
