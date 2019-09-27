.. image:: ../images/Spacex_067.jpg
   :scale: 50 %

Source: [Ref4]_

History Information
*******************

This group of API calls will enable the retrieval of history data. History data is classed as significant steps forward in SpaceX's journey toward commercial spaceflight
ALL history calls can be given a set of parameters, with which to modify the response.
Like all functions in this module, the API parameters must be given as a JSON payload such as can be seen :doc:`here <jsonpayload>`.

All historic events
```````````````````

.. code-block:: python

    history = spacexpython.history.history(parameters,timeOut)
    print(history)

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

`Valid parameters <https://docs.spacexdata.com/?version=latest#9f1dfdc0-fbe8-4ae5-9209-7f3d649a627c>`_

Specific Historic event
```````````````````````

.. code-block:: python

    event = spacexpython.history.one(event_id,parameters,timeOut)
    print(event)

Parameters:

.. tabularcolumns:: |1|1|C|C|

+------------+-------------------------------------------+-----------+---------+
| Name       | Purpose                                   | Mandatory | Default |
+============+===========================================+===========+=========+
| event_id   | ID of the historic event                  |      Y    |         |
+------------+-------------------------------------------+-----------+---------+
| parameters | JSON list of URL qualifiers in the form   |      N    |         |
+            +                                           +           +         +
|            | {"status":"active","limit":3 ......etc    |           |         |
+------------+-------------------------------------------+-----------+---------+
| timeOut    | Number of seconds to wait until a timeout |      N    |    1    |
+------------+-------------------------------------------+-----------+---------+

`Valid parameters <https://docs.spacexdata.com/?version=latest#0eceecb8-c6e1-4e73-92e1-6dadbdbcb9da>`_

.. [Ref4] The second-stage Kestrel engine glows red-hot during Falcon 1's fourth launch and first successful orbital flight.