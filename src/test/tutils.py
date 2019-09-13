"""Utilities module for the test suite

This is a utilities module with common functionality which is used by many
other modules.

This file is imported as a module and contains the following
functions:

    * readJSONFile - reads a JSON file into a value
    * writeJSONFile - writes a JSON document into a named file
    * keyOrder - orders a JSON document by key (for lists.....)
    * alphaOrder - order a JSON document by alphabetic key name
"""

import json

import requests


def keyOrder(JSONDocument,ky):
    """ Orders a JSON Document by key order

    Parameters
    ----------
    JSONDocument
        unsorted JSON Document
    ky
        key by which the JSON document should be ordered

    Returns
    -------
    response
        the JSON document ordered by key
    """
    return json.loads(JSONDocument).sort( key=lambda k: k[ky],reverse=False)

def alphaOrder(JSONDocument):
    """ Orders a JSON Document by alphabetic key

    Parameters
    ----------
    JSONDocument
        unsorted (alphabetically) JSON Document

    Returns
    -------
    response
        the JSON document ordered by alphabetic key
    """

    return json.dumps(JSONDocument,sort_keys=True)

def readJSONFile(filename):
    """ Reads a named JSON file and retrieves the document from it.

    Parameters
    ----------
    filename : str
        name of the file

    Returns
    -------
    response
        the JSON document read from the file
    """
    filename='data/'+filename
    with open(filename) as json_file:
        response=json.load(json_file)
    return response

def writeJSONFile(filename,JSONDocument):
    """ Writes a JSON document to a named file

    Parameters
    ----------
    filename : str
        name of the file
    JSONDocument : str
        JSON document to write to the file

    Returns
    -------
    True
    """

    filename='data/'+filename
    with open(filename, 'w') as outfile:
        json.dump(JSONDocument, outfile)
    return True

def writeFile(filename,data,mode):
    """ Writes/appends data to a file

    Parameters
    ----------
    filename : str
        name of the file
    data : str
        text to write to the file

    Returns
    -------
    True
    """

    with open(filename, mode) as outfile:
        outfile.write(data)
    return True

def makeHTTP(requestUrl,timeOut=1):
    """ sends a request to an http(s) endpoint

    Parameters
    ----------
    requestUrl : str
        url to call
    timeOut : int
        optional - call timeout

    Returns
    -------
    response
        a string which is a string returned from the http call

    Exceptions
    ----------
        SpaceXReadTimeOut
            an exception raised when the API call breaches the timeout limit
    """
    try:
        url_response = requests.get(url=str(requestUrl), timeout=timeOut, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                                    )
    except requests.exceptions.ReadTimeout:
        raise TimeoutError('HTTP Timeout Error')
    else:
        response = url_response.text
    return response

def percentage(percent, whole):
    return (percent * whole) / 100.0

def plus_percent(percent, value):
    return value + percentage(percent, value)

def minus_percent(percent, value):
    return value - percentage(percent, value)