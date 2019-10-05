.. image:: ../images/falcon9launch.gif
   :scale: 100 %


Source: `SpaceX <https://spacex.com>`_ [Ref10]_

Rocket Information
******************

This group of API calls will enable the retrieval of data about the rockets that SpaceX has used over its' launch timeframe.
ALL these calls can be given a set of parameters, with which to modify the response.
Like all functions in this module, the API parameters must be given as a JSON payload such as can be seen :doc:`here <./useful/jsonpayload>`.

All Rockets
````````````

.. code-block:: python

    rockets = spacexpython.rockets.rockets(parameters,timeOut)
    print(rockets)

Parameters:

.. tabularcolumns:: |1|1|C|C|

+------------+-------------------------------------------+-----------+---------+
| Name       | Purpose                                   | Mandatory | Default |
+============+===========================================+===========+=========+
| parameters | JSON list of URL qualifiers in the form   |      N    |         |
+            +                                           +           +         +
|            | {"status":"active","limit":3 ......etc    |           |         |
+------------+-------------------------------------------+-----------+---------+
| timeOut    | Number of seconds to wait until a timeout |      N    |    1    |
+------------+-------------------------------------------+-----------+---------+

`Valid parameters <https://docs.spacexdata.com/?version=latest#16c58b5e-44de-4183-b858-0fae51d242a5>`_

Specific Rocket
```````````````

.. code-block:: python

    rocket = spacexpython.rockets.rocket(rocket_id,parameters,timeOut)
    print(rocket)

.. Note::

    The `rocket_id` parameter is one of :

    +-------------+---------------------+
    | Value       | Meaning             |
    +=============+=====================+
    | falcon1     | Falcon 1 Rocket     |
    +-------------+---------------------+
    | falcon9     | Falcon 1 Rocket     |
    +-------------+---------------------+
    | falconheavy | Falcon Heavy Rocket |
    +-------------+---------------------+
    | bfr         | Big Falcon Rocket   |
    +-------------+---------------------+
    | starship    | Starship            |
    +-------------+---------------------+

Parameters:

.. tabularcolumns:: |1|1|C|C|

+---------------+-------------------------------------------+-----------+---------+
| Name          | Purpose                                   | Mandatory | Default |
+===============+===========================================+===========+=========+
| rocket_id     | ID of the rocket                          |      Y    |         |
+---------------+-------------------------------------------+-----------+---------+
| parameters    | JSON list of URL qualifiers in the form   |      N    |         |
+               +                                           +           +         +
|               | {"status":"active","limit":3 ......etc    |           |         |
+---------------+-------------------------------------------+-----------+---------+
| timeOut       | Number of seconds to wait until a timeout |      N    |    1    |
+---------------+-------------------------------------------+-----------+---------+

An additional method of acquiring information about a specific rocket would be to use the rocket-specific functions:

.. code-block:: python

    falcon1     = spacexpython.rockets.falcon1(parameters,timeOut)
    falcon9     = spacexpython.rockets.falcon9(parameters,timeOut)
    falconheavy = spacexpython.rockets.falconheavy(parameters,timeOut)
    bfr         = spacexpython.rockets.bfr(parameters,timeOut)
    starship    = spacexpython.rockets.starship(parameters,timeOut)


`Valid parameters <https://docs.spacexdata.com/?version=latest#eda45a06-9f05-40f1-a333-028f647ba797>`_

.. note::

    Beginning with version 1.1.1.a1, any references to "bfr" will cause the information from the "starship" function to be returned. This is because Elon Musk, on the 20th November 2018 renamed Big Falcon Rocket to Starship. [RefBFR]_

    Additionally, as of version 1.1.2, any reference to 'bfr' will be removed. Thus, at this time, those references are considered to be deprecated.

.. [Ref10]  Launch of Falcon 9 for mission CRS-12 14th August 2017

.. [RefBFR] `BBC News Story <https://www.bbc.co.uk/news/business-46274158>`_