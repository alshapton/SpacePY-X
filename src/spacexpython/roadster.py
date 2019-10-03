from . import urldata
from . import utils


def roadster(timeOut=1):
    """

    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_roadster
    return utils.makeRequest(requestUrl, timeOut)
