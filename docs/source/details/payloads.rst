.. image:: ../images/nicer.gif
   :scale: 100 %

Source: `NASA <https://www.nasa.gov/press-release/goddard/2017/nasa-neutron-star-mission-begins-science-operations>`_ [Ref9]_

Payload Information
*******************

This group of API calls will enable the retrieval of data about the various payloads that SpaceX has (or will be) responsible for shipping.
ALL these calls can be given a set of parameters, with which to modify the response.
Like all functions in this module, the API parameters must be given as a JSON payload such as can be seen :doc:`here <./useful/jsonpayload>`.

All Payloads
````````````

.. code-block:: python

    payloads = spacexpython.payloads.payloads(parameters,timeOut)
    print(payloads)

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

`Valid parameters <https://docs.spacexdata.com/?version=latest#81150545-5ab3-4552-b1f5-865b7f542033>`_

Specific Payload
````````````````

.. code-block:: python

    payload = spacexpython.payloads.one(payload_id,parameters,timeOut)
    print(payload)

Parameters:

.. tabularcolumns:: |1|1|C|C|

+---------------+-------------------------------------------+-----------+---------+
| Name          | Purpose                                   | Mandatory | Default |
+===============+===========================================+===========+=========+
| payload_id    | ID of the payload                         |      Y    |         |
+---------------+-------------------------------------------+-----------+---------+
| parameters    | JSON list of URL qualifiers in the form   |      N    |         |
+               +                                           +           +         +
|               | {"status":"active","limit":3 ......etc    |           |         |
+---------------+-------------------------------------------+-----------+---------+
| timeOut       | Number of seconds to wait until a timeout |      N    |    1    |
+---------------+-------------------------------------------+-----------+---------+

`Valid parameters <https://docs.spacexdata.com/?version=latest#290f98df-e218-4635-9012-4657cd51f67e>`_

.. [Ref9]  This time-lapse animation shows NICER being extracted from the SpaceX Dragon trunk on June 11, 2017