Exceptions
**********

Should an error occur anywhere in the call to a function (whether that be in the wrapper or the REST API itself), an
exception will be raised.

All normal Python exceptions exist that can be trapped, however, the wrapper implements a new exception:

.. code-block:: python

    SpaceXReadTimeOut


This exception occurs when the API times out for any reason. It can be trapped, and possibly a retry or other action
performed as appropriate, for example:

.. code-block:: python

    try:
        capsules_data = keyOrder(alphaOrder(spacexpython.capsules.capsules('',1)),'capsule_serial')
    except spacexpython.utils.SpaceXReadTimeOut:
        print("Failure on retriueval of capsule information")


