from . import urldata
from . import utils


def launchpads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_launchpads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(pad='',parameters='', timeOut=1):
    """

    :type pad: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_launchpads + "/" + pad
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

