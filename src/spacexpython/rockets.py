import requests
import urldata
import utils

def all():
    requestUrl = urldata.Domain.main + urldata.Domain.main_rockets
    return utils.makeRequest(requestUrl)

def falcon1():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_1
    return utils.makeRequest(requestUrl)

def falcon9():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_9
    return utils.makeRequest(requestUrl)

def falconHeavy():
    requestUrl = urldata.Domain.main + urldata.Domain.falcon_heavy
    return utils.makeRequest(requestUrl)

def bfr():
    requestUrl = urldata.Domain.main + urldata.Domain.big_falcon_rocket
    return utils.makeRequest(requestUrl)
