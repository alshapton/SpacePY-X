import urldata
import requests
import json

def jsonParameters(parameters):
    jsonObject=json.loads(parameters)
    for key in jsonObject:
        value=jsonObject[key]
        parms=key+'='+value+'&'
    return parms[:-1]


def makeRequest(requestUrl):
    url_response = requests.get(url=str(requestUrl), timeout=1)
    response = url_response.json()
    return response

