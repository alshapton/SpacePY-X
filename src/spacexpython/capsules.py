import urldata
import utils

def capsules(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + '?' + utils.jsonParameters(parameters)
    return utils.makeRequest(requestUrl,timeOut)

def upcoming(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_capsules
    return utils.makeRequest(requestUrl,timeOut)

def past(parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.past_capsules
    return utils.makeRequest(requestUrl,timeOut)

def one(capsule_id,parameters='',timeOut=1):
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + "/" + str(capsule_id)
    return utils.makeRequest(requestUrl,timeOut)
