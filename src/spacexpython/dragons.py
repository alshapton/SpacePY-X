from . import urldata
from . import utils


def dragons(parameters='', timeOut=1):
        """

        :type parameters: Optional[str]
        :type timeOut: Optional[int]

        """
        requestUrl = urldata.Domain.main + urldata.Domain.main_dragons
        return utils.makeRequest(requestUrl, timeOut, parameters)

def one(dragon='',parameters='', timeOut=1):
        """

        :type dragon: str
        :type parameters: Optional[str]
        :type timeOut: Optional[int]

        """
        requestUrl = urldata.Domain.main + urldata.Domain.main_dragons + "/" + dragon
        return utils.makeRequest(requestUrl, timeOut, parameters)
