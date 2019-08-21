from . import urldata
from . import utils


def dragons(parameters='', timeOut=1):
        requestUrl = urldata.Domain.main + urldata.Domain.main_dragons
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(dragon='',parameters='', timeOut=1):
        requestUrl = urldata.Domain.main + urldata.Domain.main_dragons + "/" + dragon
        return utils.makeRequest(requestUrl, timeOut, parameters)
