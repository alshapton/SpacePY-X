.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   details/usage.rst
   details/capsules.rst
   details/jsonpayload.rst
   details/exceptions.rst
   details/cores.rst

***********************************************************************************************
Simple and Easy API Wrapper for `r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`_
***********************************************************************************************

Documentation
*************
This API Wrapper aims to provide a simple and easy
way to use the `SpaceX-API <https://github.com/r-spacex/SpaceX-API>`_ in Python projects.

.. rubric:: Installation: Note that this supports Python 3 *ONLY*

To install via pip use: pip install spacePY-X

.. rubric:: Authentication

No authentication is currently required by `r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`_ to use this public API and thus is not required in this wrapper.

.. rubric:: Rate Limiting

The API has a rate limit of 50 req/sec per IP
address, if exceeded, a response of 429 will be given until the rate drops back below 50 req/sec.

.. rubric:: Credits

Jake Meyer's `r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`_

Based on work by `vinayphadnis <https://github.com/vinayphadnis/SpaceX-Python.git>`_

.. rubric:: License MIT
