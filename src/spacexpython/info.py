from . import urldata
from . import utils
import pyjsonq


def company(timeOut=1):
    """

    :type timeOut: Optional[int]

    """
    utils.validateParameters('', __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_info
    return utils.makeRequest(requestUrl, timeOut)


def api(timeOut=1):
    """

    :type timeOut: Optional[int]

    """
    utils.validateParameters('', __name__, utils.func_name())
    requestUrl = urldata.Domain.main + urldata.Domain.main_api
    return utils.makeRequest(requestUrl, timeOut)


def clients(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """

    # utils.validateParameters('', __name__, utils.func_name())
    return utils.getAPISupporting("clients", parameters, timeOut)
