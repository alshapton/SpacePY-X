import requests
import urldata
import utils

def company():
    requestUrl = urldata.Domain.main + urldata.Domain.main_info
    return utils.makeRequest(requestUrl)

def api():
    requestUrl = urldata.Domain.main + urldata.Domain.main_api
    return utils.makeRequest(requestUrl)
