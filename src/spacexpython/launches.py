from . import urldata
from . import utils

def all(parameters='',timeOut=1):
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl,timeOut,parameters)

def latest(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def nextlaunch(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def upcoming(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)
