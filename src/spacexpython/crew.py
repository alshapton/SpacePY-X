from . import urldata
from . import utils

def crew(timeOut=1):
    """

    :type timeOut: Optional[int]

    """
    requestUrl = urldata.Domain.main + urldata.Domain.main_crew
    return utils.makeRequest(requestUrl,timeOut)
