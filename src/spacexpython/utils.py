"""Utilities module

This is a utilities module with common functionality
which is used by many other modules.

This file is imported as a module and contains the following
functions:

    * jsonParameters - converts a JSON document
                        into a URL parameter string
    * makeRequest - function to call a REST api
    * getAPISupporting - Get information from API support page
    * validateParameters - validate parameters to any API functions

    * Internal Functions:
        -   func_name
        -   clients
        -   apps

"""
import ast
import json
import sys
import requests
import cachepy
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage


sys.path.append('../')

from .exceptions import *


clientcache = cachepy.Cache()
APIcache = cachepy.Cache()
appcache = cachepy.Cache()


def jsonParameters(parameters):
    """

    :type parameters: str

    converts a JSON document into a URL parameter string

    Parameters
    ----------
    parameters : JSON document (str)
        JSON document containing the list
        of parameters to add to the API call

    Returns
    -------
    parms
        a string which can be appended to the URL
    """
    if (parameters == ''):
        return ''
    else:
        jsonObject = json.loads(parameters)
        parms = '?'
        for key in jsonObject:
            value = jsonObject[key]
            parms = parms + key + '=' + value + '&'
        return parms[:-1]


def makeRequest(requestUrl, timeOut=1, parameters=''):
    """
    :param requestUrl: str
    :param timeOut: Optional[str]
    :param parameters: Optional[str]
    :return: object:

    Sends a request to the API

    Parameters
    ----------
    requestURL : str
        string to pass into the REST API
    timeOut : int
        optional - API call timeout
    parameters : str
        optional parameters to append to URL as query modifiers

    Returns
    -------
    response
        a string which is a JSON document returned from the API

    Exceptions
    ----------
    SpaceXReadTimeOut
        raised when the API call breaches the timeout limit
    """

    try:
        url_response = requests.get(url=str(requestUrl)
                                    + jsonParameters(parameters),
                                    timeout=timeOut)
    except requests.exceptions.ReadTimeout:
        raise SpaceXReadTimeOut('Space/X Timeout Error')
    else:
        response = url_response.json()
    return response


@clientcache
def buildclients(url_response):
    """
    :param url_response: str

    Parameters
    ----------
    :param url_response: str

    Returns
    -------
    clientDB
        An in-memory TinyDB instance containing clients

    """
    # Storage for clients will be in an in-memory TinyDB
    clientDB = TinyDB(storage=MemoryStorage)

    page = BeautifulSoup(url_response.text, 'html.parser')
    table = page.find('tbody')

    for trow in table.find_all('tr')[0:]:
        tds = trow.find_all('td')

        # Split languages and form JSON Array
        initLangs = tds[1].text.split("/")
        languages = "["
        for lang in initLangs:
            languages = languages + '"' + lang.strip() + '",'
        languages = languages[:-1] + "]"

        # Split repo types and form JSON Array
        initRepos = tds[3].text.split(",")
        repotypes = "["
        for repo in initRepos:
            repotypes = repotypes + '"' + repo.strip() + '",'
        repotypes = repotypes[:-1] + "]"

        # Split Creators and form JSON Array
        initcreators = tds[2].text.split(",")
        creators = "["
        for creator in initcreators:
            creators = creators + '"' + creator.strip() + '",'
        creators = creators[:-1] + "]"

        # Split links and form JSON Array
        lnks = ''
        for lnk in tds[3].find_all('a', href=True):
            lnks = lnks + ',' + '"' + lnk['href'] + '"'
        lnks = '[' + lnks[1:] + "]"

        # insert the record into the database
        record = '{"Name":"' + tds[0].text + '","Languages":' \
                 + languages + ',"Creators":' + creators \
                 + ',"Repos":' + repotypes \
                 + ',"ReposLinks":' + lnks + '}'
        clientDB.insert(json.loads(record))

    return clientDB


@appcache
def buildapps(url_response):
    """
    :param url_response: str

    Parameters
    ----------
    :param url_response: str

    Returns
    -------
    appsDB
        An in-memory TinyDB instance containing apps

    """
    # Storage for apps will be in an in-memory TinyDB
    appsDB = TinyDB(storage=MemoryStorage)

    page = BeautifulSoup(url_response.text, 'html.parser')
    name_box = page.find('tbody')
    print(name_box)
    for trow in name_box.find_all('tr')[0:]:
        tds = trow.find_all('td')

        # Get links for app/website etc and form JSON Array
        lnks = ''
        for lnk in tds[0].find_all('a', href=True):
            lnks = lnks + ',' + '"' + lnk['href'] + '"'
        lnks = '[' + lnks[1:] + "]"

        type = ''
        platform = ''
        # Separate Types out and deal with platforms:
        if ("WEBSITE" in (tds[1].text).upper()):
            type = type + ',"WEBSITE"'
            platform = platform + ',"WEB"'
            
        if ("ALEXA SKILL" in (tds[1].text).upper()):
            type = type + ',"ALEXA"'
            platform = platform + ',"ALEXA"'
        
        if ("ANDROID APP" in (tds[1].text).upper()):
            type = type + ',"APP"'
            platform = platform + ',"ANDROID"'

        if ("IOS APP" in (tds[1].text).upper()):
            type = type + ',"APP"'
            platform = platform + ',"IOS"'

        if ("DISCORD BOT" in (tds[1].text).upper()):
            type = type + ',"BOT"'
            platform = platform + ',"DISCORD"'

        if ("API" in (tds[1].text).upper()):
            type = type + ',"API"'
            platform = platform + ',"API"'

        if ("APPS" in (tds[1].text).upper()):
            type = type + ',"APP"'
            platform = platform + ',"IOS","ANDROID"'

        type = '[' + type[1:] + "]"
        platform = '[' + platform[1:] + "]"

        # Split Creators and form JSON Array
        initcreators = tds[2].text.split(",")
        creators = "["
        for creator in initcreators:
            creators = creators + '"' + creator.strip() + '",'
        creators = creators[:-1] + "]"

        # Split "More" and form JSON Array
        initmore = tds[4].text.split(",")
        mores = '['
        for more in initmore:
            mores = mores + '"' + more.strip().replace("\""," ") + '",'
        mores = mores[:-1] + "]"
        if (mores == '[""]'):
            mores = '[]'

        # Get links for app/website etc and form JSON Array
        clnks = ''
        for lnk in tds[2].find_all('a', href=True):
            clnks = clnks + ',' + '"' + lnk['href'] + '"'
        clnks = '[' + clnks[1:] + "]"

        app = tds[0].text

        # Split "Repos" and form JSON Array
        initrepo = tds[3].text.split(",")
        repos = '['
        for repo in initrepo:
            repos = repos + '"' + repos.strip() + '",'
        repos = repos[:-1] + "]"
        if (repos == '[""]'):
            repos = '[]'

        # Get links for repo and form JSON Array
        rlnks = ''
        for lnk in tds[3].find_all('a', href=True):
            rlnks = rlnks + ',' + '"' + lnk['href'] + '"'
        rlnks = '[' + rlnks[1:] + "]"

        # Get more links for repo and form JSON Array
        mlnks = ''
        for lnk in tds[4].find_all('a', href=True):
            mlnks = mlnks + ',' + '"' + lnk['href'] + '"'
        mlnks = '[' + mlnks[1:] + "]"

        record = '{"Name":"' + app + '","Links":' \
                 + lnks + ',"Types":' + type \
                 + ',"Platforms":' + platform \
                 + ',"Creators":' + creators \
                 + ',"CreatorsLinks":' + clnks \
                 + ',"Repos":' + rlnks \
                 + ',"ReposLinks":' + rlnks \
                 + ',"More":' + mores \
                 + ',"MoreLinks":' + mlnks + '}'
        appsDB.insert(json.loads(record))
    return appsDB


@APIcache
def getAPISupporting(req, parameters, timeOut=1):
    """
    :param req: str
    :param parameters: Optional[str]
    :param timeOut: Optional[str]

    Parameters
    ----------
    req : str
        whether clients or apps are required
    parameters : str
        optional parameters use as query modifiers
    timeOut : int
        optional - API call timeout

    Returns
    -------
    response
        a string which is a JSON document returned from the
        APISupport page

    Exceptions
    ----------
    SpaceXReadTimeOut
        raised when the API call breaches the timeout limit
    """

    global clientDB
    global appsDB

    base = "https://github.com/r-spacex/SpaceX-API/blob/master/docs/"
    requestUrl = base + req + ".md"
    try:
        url_response = requests.get(url=str(requestUrl),
                                    timeout=timeOut)
    except requests.exceptions.ReadTimeout:
        raise SpaceXReadTimeOut('Space/X Timeout Error')
    else:
        if (req == 'clients'):
            # If the list of clients hasnt been built, build it
            try:
                # noinspection PyUnresolvedReferences
                clientDB
            except (NameError, UnboundLocalError):
                clientDB = buildclients(url_response)

            if (parameters == ''):
                # Make sure that here we read all the
                # records from the database into a JSON string
                responseT = str(clientDB.all())
                response = responseT.replace("'", "\"")
            else:
                # When there are parameters:
                Row = Query()  # noqa
                query = ''
                parametersJSON = json.loads(parameters)

                for key, value in parametersJSON.items():
                    query = query + "(Row." + str(key).capitalize() \
                        + ".any(" + str(value) + ")) & "
                query = query[:-2]
                print(query)
                responseT = clientDB.search(eval(query))
                response = str(responseT).replace("'", "\"")

        if (req == 'apps'):
            # If the list of apps hasnt been built, build it
            try:
                # noinspection PyUnresolvedReferences
                appsDB
            except (NameError, UnboundLocalError):
                appsDB = buildapps(url_response)

            if (parameters == ''):
                # Make sure that here we read all the
                # records from the database into a JSON string
                responseT = str(appsDB.all())
                response = str(responseT).replace("'", "\"")
            else:
                # When there are parameters:
                Row = Query()  # noqa
                query = ''
                parametersJSON = json.loads(parameters)

                for key, value in parametersJSON.items():
                    query = query + "(Row." + str(key).capitalize() \
                        + ".any(" + str(value) + ")) & "
                query = query[:-2]
                print(query)
                responseT = appsDB.search(eval(query))
                response = str(responseT).replace("'", "\"")

        if ((req != 'apps') and (req != "clients") and (req != '')):
            raise SpaceXParameterError

    return json.loads(response)


def validateParameters(inParameters, inFunction, subfunction):
    # If there are no parameters, then nothing needs validating.
    if (inParameters == ''):
        return True
    parameters = ast.literal_eval(inParameters)
    # Get the function name from the call
    discard, function = inFunction.split('.')

    # Open the database
    db = TinyDB('matrixDB.json')
    # Get the list of rows for this function/subfunction
    Row = Query()
    subFunctionLine = db.get((Row.function == function)
                             & (Row.subfunction == subfunction))

    functionParameters = subFunctionLine.get("parameters")
    fp = []
    ft = []

    cfp = 0
    # get list of parameters in function/subfunction
    # and populate 2 lists with their names and types
    for i in functionParameters:
        cfp = cfp + 1
        fp.append(i.get("parameter"))
        ft.append(i.get("parameter") + ".<class '"
                  + i.get("type") + "'>")

    # if there are no parameters applicable
    # for this function, return true
    if (cfp == 0):
        return True

    # Go though list of supplied parameters,
    # testing each for name validity and type validity
    for key, value in parameters.items():
        if key not in fp:
            raise SpaceXParameterError(key
                                       + " is not a valid parameter for "  # noqa
                                       + function + "."
                                       + subfunction)
        else:

            for g in ft:
                p, t = g.split('.')
                if (p == key):
                    break

            if (t == "<class 'int'>"):
                try:
                    attempt = int(value)
                    break
                except ValueError:
                    raise SpaceXParameterError("Type '"
                                               + str(type(value))
                                               .replace("<class '", "")
                                               .replace("'>", "")
                                               + "' is not valid for "
                                               + function + "."
                                               + subfunction
                                               + "(parameter: "
                                               + key + ")")

            if (t == "<class 'bool'>"):
                if (value.upper() not in ['TRUE', 'FALSE']):
                    raise SpaceXParameterError("Type '"
                                               + str(type(value)).
                                               replace("<class '", "").
                                               replace("'>", "")
                                               + "' is not valid for "
                                               + function + "."
                                               + subfunction
                                               + "(parameter: "
                                               + key + ")")
            else:
                # if the parameter is of the incorrect
                # type then raise an exception
                if (key + "." + str(type(value))) not in ft:
                    raise SpaceXParameterError("Type '"
                                               + str(type(value)).
                                               replace("<class '", "").
                                               replace("'>", "")
                                               + "' is not valid for "
                                               + function + "."
                                               + subfunction
                                               + "(parameter: "
                                               + key + ")")
    # If every parameter and type combination work out then good to go !
    return True


def func_name():
    # Source: https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback  # noqa
    currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
    return currentFuncName(1)
