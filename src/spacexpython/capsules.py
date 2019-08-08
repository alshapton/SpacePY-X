import urldata
import json
import utils

def capsules(parameters=''):
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + '?' + utils.jsonParameters(parameters)
    return utils.makeRequest(requestUrl)

def upcoming():
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_capsules
    return utils.makeRequest(requestUrl)

def past():
    requestUrl = urldata.Domain.main + urldata.Domain.past_capsules
    return utils.makeRequest(requestUrl)

def one(capsule_id):
    requestUrl = urldata.Domain.main + urldata.Domain.main_capsules + "/" + str(capsule_id)
    return utils.makeRequest(requestUrl)
