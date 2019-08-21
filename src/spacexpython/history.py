from . import urldata
from . import utils


def history(parameters='', timeOut=1):
        requestUrl = urldata.Domain.main + urldata.Domain.main_history
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(event='',parameters='', timeOut=1):
        requestUrl = urldata.Domain.main + urldata.Domain.main_history + "/" + event
        return utils.makeRequest(requestUrl, timeOut, parameters)
