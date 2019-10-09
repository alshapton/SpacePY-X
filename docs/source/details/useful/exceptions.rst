Exceptions
**********

Should an error occur anywhere in the call to a function (whether that be in the wrapper or the REST API itself), an
exception will be raised.

All normal Python exceptions exist that can be trapped, however, the wrapper implements 2 new exceptions:

.. code-block:: python

    SpaceXReadTimeOut


This exception occurs when the API times out for any reason. It can be trapped, and possibly a retry or other action
performed as appropriate, for example:

.. code-block:: python

    try:
        capsules_data = keyOrder(alphaOrder(spacexpython.capsules.capsules('',1)),'capsule_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        print("Failure on retrieval of capsule information")



..code-block:: python

    SpaceXParameterError

This exception occurs when the the paramaters for a wrapper call (and ultimately to the API itself) do not meet the type specifications set out in the core API definition:

.. code-block:: python

    try:
        coresP_data = alphaOrder(spacexpython.cores.cores('{"core_serial":"B1037","block":"true"}'))
    except spacexpython.utils.SpaceXParameterError:
        print("Incorrect parameter")


This error is due to the ``block`` parameter in this instance showing ``true`` when the parameter is defined as an ``integer``.

A further example :

.. code-block:: python

    try:
        coresP_data = alphaOrder(spacexpython.cores.cores('{"core_serial":"B1037","desired-block":"4"}'))
    except spacexpython.utils.SpaceXParameterError:
        print("Incorrect parameter")


This error is due to the ``block`` parameter in this instance not being a valid parameter.
