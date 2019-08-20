from . import urldata
from . import utils


def dragons(parameters='', timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_dragons
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)
