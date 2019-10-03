from . import urldata
from . import utils


def landingpads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_landingpads
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
        requestUrl = urldata.Domain.main + urldata.Domain.main_landingpads + "/" + pad
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

