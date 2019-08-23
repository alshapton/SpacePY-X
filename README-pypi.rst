SpaceX API wrapper in Python
============================

.. raw:: html

   <div align="center">
   <img src="https://github.com/alshapton/SpacePY-X/blob/master/pyrocket.png">

   <br>

   </div>

## Simple and Easy API Wrapper for [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)


Documentation
~~~~~~~~~~~~~

This API Wrapper aims to provide a simple and easy way to use the
`SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__ in Python
projects.
See the `Wiki <https://github.com/alshapton/SpacePY-X/wiki>`__ for full
wrapper documentation.

Installation
~~~~~~~~~~~~

Note that this supports Python 3 *ONLY*

To install via ``pip`` use:
``pip install spacexPython``

Basic Usage
~~~~~~~~~~~

The usage of the wrapper is very easy. It does not require any
initialisation. Just import and start coding:
\`\`\`python
import spacexpython

rocket\_data = spacexpython.rockets.falconHeavy()
print(rocket\_data)
\`\`\`

Credits
~~~~~~~

Jake Meyer's
`r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__

Based on work by
`vinayphadnis <https://github.com/vinayphadnis/SpaceX-Python.git>`__

License
~~~~~~~

|FOSSA Status|

.. |FOSSA Status| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X.svg?type=large
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X?ref=badge_large
