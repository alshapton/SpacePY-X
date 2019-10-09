from . import urldata
from . import utils


def payloads(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_payloads
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(payload='',parameters='', timeOut=1):
    """

    :type payload: str
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    utils.validateParameters(parameters, __name__, utils.func_name())
    try:
        requestUrl = urldata.Domain.main + urldata.Domain.main_payloads + "/" + payload
    except utils.SpaceXReadTimeOut as e:
        raise e
    else:
        return utils.makeRequest(requestUrl, timeOut, parameters)

