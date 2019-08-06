import requests
import urldata
import utils



def launches():
    requestUrl = urldata.Domain.main + urldata.Domain.main_launches
    return utils.makeRequest(requestUrl)

def latest():
    requestUrl = urldata.Domain.main + urldata.Domain.latest_launches
    return utils.makeRequest(requestUrl)

def next():
    requestUrl = urldata.Domain.main + urldata.Domain.next_launches
    return utils.makeRequest(requestUrl)

def upcoming():
    requestUrl = urldata.Domain.main + urldata.Domain.upcoming_launches
    return utils.makeRequest(requestUrl)
