from . import urldata
from . import utils


def payloads(parameters='', timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_payloads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(payload='',parameters='', timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_payloads + "/" + payload
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

