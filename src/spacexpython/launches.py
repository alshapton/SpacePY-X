from . import urldata
from . import utils

def alllaunches(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl,timeOut,parameters)

def latest(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def nextlaunch(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def upcoming(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def past(parameters='',timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.past_launches
    return utils.makeRequest(requestUrl,timeOut,parameters)

def one(launch='',parameters='',timeOut=1):
    """

    :tyoe launch: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain + "/" + launch
    return utils.makeRequest(requestUrl,timeOut,parameters)
