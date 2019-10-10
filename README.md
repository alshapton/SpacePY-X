# SpaceX API wrapper in Python
<div align="center">
<img src="https://github.com/alshapton/SpacePY-X/blob/master/pyrocket.png">


[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors)
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
See the [Documentation](https://spacepy-x.readthedocs.io/en/master/) for full wrapper documentation.

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
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="http://fossa.io"><img src="https://avatars0.githubusercontent.com/u/29791463?v=4" width="100px;" alt="fossabot"/><br /><sub><b>fossabot</b></sub></a><br /><a href="#review-fossabot" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://www.vphadnis.com"><img src="https://avatars0.githubusercontent.com/u/21256352?v=4" width="100px;" alt="Vinay Phadnis"/><br /><sub><b>Vinay Phadnis</b></sub></a><br /><a href="https://github.com/alshapton/SpacePY-X/commits?author=vinayphadnis" title="Code">💻</a></td>
    <td align="center"><a href="https://pyup.io"><img src="https://avatars0.githubusercontent.com/u/16239342?v=4" width="100px;" alt="pyup.io bot"/><br /><sub><b>pyup.io bot</b></sub></a><br /><a href="#review-pyup-bot" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://www.codacy.com"><img src="https://avatars3.githubusercontent.com/u/23704769?v=4" width="100px;" alt="Codacy Badger"/><br /><sub><b>Codacy Badger</b></sub></a><br /><a href="#review-codacy-badger" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/alshapton/SpacePY-X/commits?author=codacy-badger" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/all-contributors/all-contributors-bot"><img src="https://avatars3.githubusercontent.com/u/46843839?v=4" width="100px;" alt="allcontributors[bot]"/><br /><sub><b>allcontributors[bot]</b></sub></a><br /><a href="https://github.com/alshapton/SpacePY-X/commits?author=allcontributors" title="Documentation">📖</a></td>
    <td align="center"><a href="https://pep8speaks.com"><img src="https://avatars1.githubusercontent.com/u/24736507?v=4" width="100px;" alt="PEP 8 Speaks"/><br /><sub><b>PEP 8 Speaks</b></sub></a><br /><a href="#review-pep8speaks" title="Reviewed Pull Requests">👀</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->


This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
