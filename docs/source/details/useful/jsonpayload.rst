JSON Parameters
***************

Most functions within thus wrapper will take a parameter (typically called "parameters").

The value is a modifier/qualifier to the function call that is being made, and will affect the results of that function.

The value should be expressed as a valid JSON payload, such as the following:

.. code-block:: json

    {
        "status":"active",
        "limit":"3"
    }

An example of this would be:

.. code-block:: python

    parameters = {"status":"active", "limit":"3"}    # JSON payload indicating only 3 active
                                                   # capsules should be returned
    timeOut = 2                                    # wait 2 seaconds before recording a timeout
    capsules = spacexpython.capsules.capsules(parameters,timeOut)
    print(capsule)

.. note::

    As of version 1.1.1a2, initial validation has been introduced. This should NOT be considered production ready yet.

    Up to and including version 1.0.0.alpha4, no parameter validation took place, therefore incorrect parameters would produce
    unknown and unpredictable effects. Please check all spelling and validity of parameters prior to use.
