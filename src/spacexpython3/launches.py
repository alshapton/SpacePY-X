
from . import urldata
from . import utils

def all(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    return utils.makeRequest(requestUrl,timeOut)

def latest(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return utils.makeRequest(requestUrl,timeOut)

def next(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return utils.makeRequest(requestUrl,timeOut)

def upcoming(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return utils.makeRequest(requestUrl,timeOut)
