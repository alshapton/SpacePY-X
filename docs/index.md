# SpaceX API wrapper in Python
<div align="center">

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c8b036f596d2471a9ce4c4e78bf9a3f3)](https://app.codacy.com/app/alshapton/SpacePY-X?utm_source=github.com&utm_medium=referral&utm_content=alshapton/SpacePY-X&utm_campaign=Badge_Grade_Settings)
[![Updates](https://pyup.io/repos/github/alshapton/SpacePY-X/shield.svg)](https://pyup.io/repos/github/alshapton/SpacePY-X/)
[![Python 3](https://pyup.io/repos/github/alshapton/SpacePY-X/python-3-shield.svg)](https://pyup.io/repos/github/alshapton/SpacePY-X/)
[![Known Vulnerabilities](https://snyk.io//test/github/alshapton/SpacePY-X/badge.svg?targetFile=requirements.txt)](https://snyk.io//test/github/alshapton/SpacePY-X?targetFile=requirements.txt)
[![Build Status](https://travis-ci.com/alshapton/SpacePY-X.svg?branch=master)](https://travis-ci.com/alshapton/SpacePY-X)
[![GitHub release](https://img.shields.io/github/release/alshapton/SpacePY-X.svg)](https://github.com/alshapton/SpacePY-X/releases)
[![GitHub issues](https://img.shields.io/github/issues/alshapton/SpacePY-X.svg)](https://github.com/alshapton/SpacePY-X/issues)
[![GitHub stars](https://img.shields.io/github/stars/alshapton/SpacePY-X.svg)](https://github.com/alshapton/SpacePY-X/stargazers)
[![GitHub license](https://img.shields.io/github/license/alshapton/SpacePY-X.svg)](https://github.com/alshapton/SpacePY-X)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X?ref=badge_shield)

## Simple and Easy API Wrapper for [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)

<br>

</div>

### Documentation
This API Wrapper aims to provide a simple and easy way to use the [SpaceX-API](https://github.com/r-spacex/SpaceX-API) in Python projects.
<br>
See the [Wiki](https://github.com/alshapton/SpacePY-X/wiki) for full wrapper documentation.

### Installation
Note that this supports Python 3 *ONLY*

To install via `pip` use:
`pip install spacexPython`

### Basic Usage
The usage of the wrapper is very easy. It does not require any initialisation. Just import and start coding:
```python
import spacexpython

rocket_data = spacexpython.rockets.falconHeavy()
print(rocket_data)
```

### Credits
Jake Meyer's [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)

Based on work by [vinayphadnis](https://github.com/vinayphadnis/SpaceX-Python.git)

### License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Falshapton%2FSpacePY-X?ref=badge_large)