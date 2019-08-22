from . import urldata
from . import utils


def missions(parameters='', timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_missions
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(mission='',parameters='', timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_missions + "/" + mission
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

