| <img src="https://github.com/alshapton/SpacePY-X/blob/master/pyrocket.png" width="200"/> | <h1><b>Introduction to SpacePY-X<b></h1>  <br>This API Wrapper aims to provide a simple and<br>easy way to use the [SpaceX-API](https://github.com/r-spacex/SpaceX-API) in Python projects.<br><br>This wiki is created to provide the documentation<br>about the functions available in SpacePY-X. <br><br>For documentation specific to the SpaceX-API, please <br>see the [documentation](https://github.com/r-spacex/SpaceX-API/wiki) on [the SpaceX-API Github Page](https://github.com/r-spacex/SpaceX-API/) |
|:----------------------------------------------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Authentication
No authentication is currently required by [r-SpaceX](https://github.com/r-spacex) to use this public API and thus is not required in this wrapper.

## Rate Limiting
The API has a rate limit of 50 req/sec per IP address, if exceeded, a response of 429 will be given until the rate drops back below 50 req/sec.

## Wrapper Usage
* [Basic Usage](Basic-Usage)

## Endpoints
* [Capsule Data](Capsules)
* [Core Data](Cores)
* [Dragon Data](Dragons)
* [History Data](History-Information)
* [Information](Information)
* [Landing Pad Data](Landing-Pads)
* [Launch Pads](Launch-Pads)
* [Launch Data](Launches)
* [Rocket Data](Rockets)