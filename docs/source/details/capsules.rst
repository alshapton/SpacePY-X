.. image:: ../images/Spacex-Dragon.jpg
   :scale: 50 %

Source: `NASA <https://nasa.gov>`_ `Images <https://images.nasa.gov/details-iss058e027464.html>`_

Capsule Information
*******************

This group of API calls will enable the retrieval of capsule data. ALL capsule calls can be given a set of parameters, with which to modify the response.
Like all functions in this module, the API parameters must be given as a JSON payload such as can be seen `here <https://en.wikipedia.org/wiki/SpaceX#Spacecraft>`_.

Get all capsule information:

.. code-block:: python

    capsules = spacexpython.capsules(parameters,timeOut)
    print(capsule)

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


Get a specific capsule information:

.. code-block:: python

    capsule = spacexpython.capsule('C112')
    print(capsule)

Get information about upcoming capsules being used:

.. code-block:: python

    upcoming_capsules = spacexpython.capsules.upcoming()
    print(upcoming_capsules)


Get information about past capsules that have been used:

.. code-block:: python

    past_capsules = spacexpython.capsules.past()
    print(past_capsules)

Base SpaceX API documentation for `Capsules <https://docs.spacexdata.com/?version=latest#d65a7f85-e0c7-41ce-b41d-9ad20a238d90>`_
