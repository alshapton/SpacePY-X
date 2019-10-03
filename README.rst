Simple and Easy API Wrapper for `r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__
------------------------------------------------------------------------------------------------


Documentation
~~~~~~~~~~~~~

This API Wrapper aims to provide a simple and easy way to use the
`SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__ in Python
projects. See the
`Documentation <https://spacepy-x.readthedocs.io/en/latest/>`__ for full
wrapper documentation.

Installation
~~~~~~~~~~~~

Note that this supports Python 3 *ONLY*

To install via ``pip`` use: ``pip install spacexPython``

Basic Usage
~~~~~~~~~~~

The usage of the wrapper is very easy. It does not require any
initialisation. Just import and start coding:

.. code:: python

    import spacexpython

    rocket_data = spacexpython.rockets.falconHeavy()
    print(rocket_data)

Credits
~~~~~~~

Jake Meyer's
`r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__

Based on work by
`vinayphadnis <https://github.com/vinayphadnis/SpaceX-Python.git>`__

License
~~~~~~~

MIT License