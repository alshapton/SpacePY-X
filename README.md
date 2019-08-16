# SpaceX API wrapper in Python
<div align="center">


[![Known Vulnerabilities](https://snyk.io//test/github/alshapton/SpacePY-X/badge.svg?targetFile=requirements.txt)](https://snyk.io//test/github/alshapton/SpacePY-X?targetFile=requirements.txt)
[![Build Status](https://travis-ci.com/alshapton/SpacePY-X.svg?branch=master)](https://travis-ci.com/alshapton/SpacePY-X)
[![GitHub release](https://img.shields.io/github/release/alshapton/SpaceX-Python.svg)](https://github.com/alshapton/SpacePY-X/releases)
[![GitHub issues](https://img.shields.io/github/issues/alshapton/SpaceX-Python.svg)](https://github.com/alshapton/SpacePY-X/issues)
[![GitHub stars](https://img.shields.io/github/stars/alshapton/SpaceX-Python.svg)](https://github.com/alshapton/SpacePY-X/stargazers)
[![GitHub license](https://img.shields.io/github/license/alshapton/SpaceX-Python.svg)](https://github.com/alshapton/SpacePY-X)

### Simple and Easy API Wrapper for [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)!

<br><br>

</div>

## Documentation
This API Wrapper aims to provide a simple and easy way to use the [SpaceX-API](https://github.com/r-spacex/SpaceX-API) in Python projects.
<br>
See the [Wiki](https://github.com/alshapton/SpaceX-Python/wiki) for full wrapper documentation.

## Installation

Note that this supports Python 3 *ONLY*

To install via `pip` use:
`pip install spacexPython`

## Basic Usage

The usage of the wrapper is very easy. It does not require any initialisation. Just import and start coding:
```python
import spacexpython

rocket_data = spacexpython.rockets.falconHeavy()
print(rocket_data)
```

## Credits

Forked from original work by [vinayphadnis](https://github.com/vinayphadnis/SpaceX-Python.git)
