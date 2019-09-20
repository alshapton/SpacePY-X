Useful Information
*******************

JSON Parameters
***************

Most functions within thus wrapper will take a parameter (typically called "parameters").

The value is a modifier/qualifier to the function call that is being made, and will affect the results of that function.

The value should be expressed as a valid JSON payload, such as the following:

.. code-block:: json

    {
        "status":"active",
        "limit":3
    }

An example of this would be:

.. code-block:: python

    parameters = {"status":"active", "limit":3}    # JSON payload indicating only 3 active
                                                   # capsules should be returned
    timeOut = 2                                    # wait 2 seaconds before recording a timeout
    capsules = spacexpython.capsules(parameters,timeOut)
    print(capsule)

.. note::

    As of version 1.0.0.alpha4, no parameter validation takes place, therefore incorrect parameters will produce
    unknown and unpredictable effects. Please check all spelling and validity of parameters prior to use.

Exceptions
**********

Should an error occur anywhere in the call to a function (whether that be in the wrapper or the REST API itself), an
exception will be raised.

All normal Python exceptions exist that can be trapped, however, the wrapper implements a new exception:

.. code-block:: python

    SpaceXReadTimeOut

This exception occurs when the API times out for any reason. It can be trapped, and possibly a retry or other action
performed as appropriate.