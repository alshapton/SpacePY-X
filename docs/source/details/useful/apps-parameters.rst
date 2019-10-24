Application function Parameters
*******************************

Each parameter is an incremental filter, thus each filter will narrow down the return set.

The value should be expressed as a valid JSON payload, such as the following:

.. code-block:: json

    {
        "Creators":"["Albert Gallileo","Sergey Zuckerberg"]",
        "Platforms":"iOS"
    }

An example of this would be:

.. code-block:: python

    parameters = {"Creators":"["Albert Gallileo",
                    "Sergey Zuckerberg"]",
                    "Platforms":"iOS"}                      # JSON payload indicating only iOS applications clients
                                                            # written by Albert Gallileo or Sergey Zuckerberg should be returned
    timeOut = 2                                             # wait 2 seconds before recording a timeout
    applications = spacexpython.info.apps(parameters,timeOut)
    print(applications)

..

The JSON-format parameter list consists of one or more of :

.. tabularcolumns:: |1|1|C|C|

+-----------------+--------------------------------------------+--------+----------------------------------+
| Key             | Meaning                                    | Type   | Example                          |
+=================+============================================+========+==================================+
| Name            | Application name                           | str    | SpaceX-GraphQL                   |
+-----------------+--------------------------------------------+--------+----------------------------------+
| Links           | Links(s) to the application name           |             NOT FILTERABLE                |
+-----------------+--------------------------------------------+--------+----------------------------------+
| Types           | Application type e.g. API, Website         | dict   | ["Website", "App", "Bot", "API"] |
+-----------------+--------------------------------------------+--------+----------------------------------+
| Platorms        | The platforms on which the application     | dict   | ["iOS", "Android", "Discord",    |
|                 | resides                                    |        |  "Web", "API"]                   |
+-----------------+--------------------------------------------+--------+----------------------------------+
| Creators        |                                            | dict   |                                  |
+-----------------+--------------------------------------------+--------+----------------------------------+
| CreatorsLinks   |                                            |             NOT FILTERABLE                |
+-----------------+--------------------------------------------+--------+----------------------------------+
| Repos           |                                            | dict   |                                  |
+-----------------+--------------------------------------------+--------+----------------------------------+
| ReposLinks      |                                            |             NOT FILTERABLE                |
+-----------------+--------------------------------------------+--------+----------------------------------+
| More            |                                            | dict   |                                  |
+-----------------+--------------------------------------------+--------+----------------------------------+
| MoreLinks       |                                            |             NOT FILTERABLE                |
+-----------------+--------------------------------------------+--------+----------------------------------+
The following is also valid syntax, and will return a complete list of clients:

.. code-block:: python

    parameters = ''                                         # ALL applications will be returned
    timeOut = 3                                             # wait 3 seconds before recording a timeout
    allapps = spacexpython.info.apps(parameters,timeOut)
    print(allapps)

..

.. Note::

    This feature is new as of v1.1.2
