from . import urldata
from . import utils


def capsules(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules
    return utils.makeRequest(requestUrl, timeOut, parameters)


def upcoming(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_capsules
    return utils.makeRequest(requestUrl, timeOut, parameters)


def past(parameters='', timeOut=1):
    """

    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.past_capsules
    return utils.makeRequest(requestUrl, timeOut, parameters)


def one(capsule_id, parameters='', timeOut=1):
    """

    :type capsule_id: [str]
    :type parameters: Optional[str]
    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + "/" + str(capsule_id)
    return utils.makeRequest(requestUrl, timeOut, parameters)
