Client function Parameters
**************************

Each parameter is an incremental filter, thus each filter will narrow down the return set.

The value should be expressed as a valid JSON payload, such as the following:

.. code-block:: json

    {
        "Name":"SpacePY-X",
        "Language":"Python"
    }
..

An example of this would be:

.. code-block:: python

    parameters = {"Creators":"Harry Schroedinger",
                    "Language":"Python"}                    # JSON payload indicating only Python clients
                                                            # written by Harry Schroedinger should be returned
    timeOut = 2                                             # wait 2 seconds before recording a timeout
    clients = spacexpython.info.clients(parameters,timeOut)
    print(clients)

..


    The JSON-format parameter list consists of one or more of :

.. tabularcolumns:: |1|1|C|C|

+------------+--------------------------------------------+--------+------------------------------+
| Key        | Meaning                                    | Type   | Example                      |
+============+============================================+========+==============================+
| Name       | Client name                                | str    | SpaceX-GraphQL               |
+------------+--------------------------------------------+--------+------------------------------+
| Languages  | Language(s) in which the client is written | dict   | ["Python", "Rust"]           |
+------------+--------------------------------------------+--------+------------------------------+
| Creators   | List of creator(s)                         | dict   | ["William deAngelis"]        |
+------------+--------------------------------------------+--------+------------------------------+
| Repos      | Nature(s) of Repo                          | dict   | ["Github", "NPM", "Website"] |
+------------+--------------------------------------------+--------+------------------------------+
| ReposLinks | Link(s) to repos detailled above           |             NOT FILTERABLE            |
+------------+--------------------------------------------+--------+------------------------------+

The following is also valid syntax, and will return a complete list of clients:

.. code-block:: python

    parameters = ''                                         # ALL clients will be returned
    timeOut = 3                                             # wait 3 seconds before recording a timeout
    clients = spacexpython.info.clients(parameters,timeOut)
    print(clients)

..

.. Note::

    This feature is new as of v1.1.2
