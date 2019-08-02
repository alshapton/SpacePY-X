import requests
import urldata


def company():
    requestUrl = urldata.Domain.main + urldata.Domain.main_info
    return makeRequest(requestUrl)

def api():
    requestUrl = urldata.Domain.main + urldata.Domain.main_api
    return makeRequest(requestUrl)

def makeRequest(requestUrl):
    url_response = requests.get(url=str(requestUrl), timeout=1)
    response = url_response.json()
    return response

