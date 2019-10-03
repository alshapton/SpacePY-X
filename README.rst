SpaceX API wrapper in Python
============================

.. raw:: html

   <div align="center">

|Codacy Badge| |Updates| |Python 3| |Known Vulnerabilities| |Build
Status| |GitHub release| |GitHub issues| |GitHub stars| |GitHub license|
|FOSSA Status|

Simple and Easy API Wrapper for `r-spacex/SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__
------------------------------------------------------------------------------------------------

.. raw:: html

   </div>

Documentation
~~~~~~~~~~~~~

This API Wrapper aims to provide a simple and easy way to use the
`SpaceX-API <https://github.com/r-spacex/SpaceX-API>`__ in Python
projects. See the
`Documentation <https://spacepy-x.readthedocs.io/en/master/>`__ for full
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

|FOSSA Status|

.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/c8b036f596d2471a9ce4c4e78bf9a3f3
   :target: https://app.codacy.com/app/alshapton/SpacePY-X?utm_source=github.com&utm_medium=referral&utm_content=alshapton/SpacePY-X&utm_campaign=Badge_Grade_Settings
.. |Updates| image:: https://pyup.io/repos/github/alshapton/SpacePY-X/shield.svg
   :target: https://pyup.io/repos/github/alshapton/SpacePY-X/
.. |Python 3| image:: https://pyup.io/repos/github/alshapton/SpacePY-X/python-3-shield.svg
   :target: https://pyup.io/repos/github/alshapton/SpacePY-X/
.. |Known Vulnerabilities| image:: https://snyk.io//test/github/alshapton/SpacePY-X/badge.svg?targetFile=requirements.txt
   :target: https://snyk.io//test/github/alshapton/SpacePY-X?targetFile=requirements.txt
.. |Build Status| image:: https://travis-ci.com/alshapton/SpacePY-X.svg?branch=master
   :target: https://travis-ci.com/alshapton/SpacePY-X
.. |GitHub release| image:: https://img.shields.io/github/release/alshapton/SpacePY-X.svg
   :target: https://github.com/alshapton/SpacePY-X/releases
.. |GitHub issues| image:: https://img.shields.io/github/issues/alshapton/SpacePY-X.svg
   :target: https://github.com/alshapton/SpacePY-X/issues
.. |GitHub stars| image:: https://img.shields.io/github/stars/alshapton/SpacePY-X.svg
   :target: https://github.com/alshapton/SpacePY-X/stargazers
.. |GitHub license| image:: https://img.shields.io/github/license/alshapton/SpacePY-X.svg
   :target: https://github.com/alshapton/SpacePY-X
.. |FOSSA Status| image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X.svg?type=shield
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X?ref=badge_shield
