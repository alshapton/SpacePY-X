## Basic Usage
### Installation
To install via `pip` use:
`pip install  spacexPython`

### Example Usage

To use the wrapper, import the module in any python file:
```python
import spacexpython

# Example usage:
rocket = spacexpython.rockets.falcon1()
print(rocket)
```

## Capsule Information
Get all capsule information:

```python
capsules = spacexpython.capsules(parameters,timeOut)
print(capsule)
```

Parameters:

| Name | Purpose   |Mandatory| Default |
|------------|----|-|--|
| parameters         | JSON list of URL qualifiers in the form {"status":"active","limit":3 ............etc |N||
| timeOut         | Number of seconds to wait until a timeout occurs|N|1|


Get a specific capsule information:
```python
capsule = spacexpython.capsule('C112')
print(capsule)
```

Get information about upcoming capsules being used:
```python
upcoming_capsules = spacexpython.capsules.upcoming()
print(upcoming_capsules)
```

Get information about past capsules that have been used:
```python
past_capsules = spacexpython.capsules.past()
print(past_capsules)
```
Base SpaceX API documentation for [Capsules](https://docs.spacexdata.com/?version=latest#d65a7f85-e0c7-41ce-b41d-9ad20a238d90)



## Core Information
Get all cores:
```python
core_data= spacexpython.cores.cores()
print(core_data)
```

Get information about one core:
```python
core_data= spacexpython.cores.one('B1042')
print(core_data)
```
Get all upcoming cores:
```python
core_data= spacexpython.cores.upcoming()
print(core_data)
```

Get past cores:
```python
core_data= spacexpython.cores.past()
print(core_data)
```

For optional parameters (must be included in a JSON document)- see [the documentation](https://docs.spacexdata.com/?version=latest#1a1acb6e-0f15-437b-ae16-dcabf24dec9f)

## Dragon Information
Get all Dragon information:
```python
dragons = spacexpython.dragons.dragons()
print(dragons)
```

Get a specific Dragon information:
```python
dragon = spacexpython.dragons.one('dragon2')
print(dragon)
```

# History Information
Get all Historical event information:
```python
all history = spacexpython.history.history()
print(all history)
```

Get a specific historical event information:
```python
event1 = spacexpython.history.one('1')
print(event1)
```

# Company Information
Get company information:
```python
company_data = spacexpython.info()
print(company_data)
```

Get API information:
```python
api_data = spacexpython.api()
print(api_data)
```

# Landing Pad Information
Get all Landing Pad information:
```python
landingpads = spacexpython.landingpads.landingpads()
print(landing pads)
```

Get a specific Landing Pad information:
```python
one = spacexpython.landingpads.one('OCISLY')
print(one)
```

# Launch Pad Information
Get all Launch Pad information:
```python
launchpads = spacexpython.launchpads.launchpads()
print(launch_pads)
```

Get a specific Launch Pad information:
```python
one = spacexpython.launchpads.one('ksc_lc_39a')
print(one)
```

# Launch Information
Get latest launch:
```python
launch_data = spacexpython.launches.latest()
print(launch_data)
```

Get the next Launch:
```python
launch_data = spacexpython.launches.next()
print(launch_data)
```

Get all upcoming launches:
```python
launch_data = spacexpython.launches.upcoming()
print(launch_data)
```

Get all upcoming and past launches:
```python
launch_data = spacexpython.launches.launches()
print(launch_data)
```

# Mission Information
Get all Mission information:
```python
missions = spacexpython.missions.missions()
print(missions)
```

Get a specific Mission information:
```python
one = spacexpython.missions.one('F3364BF')
print(one)
```

# Roadster Information
Get Tesla Roadster information:
```python
roadster = spacexpython.roadster.roadster()
print(roadster)
```

# Rocket Information
Get all rocket information:
```python
rocket_data = spacexpython.rockets.rockets()
print(rocket_data)
```

Get information about the Falcon 1:
```python
rocket_data = spacexpython.rockets.falcon1()
print(rocket_data)
```

Get information about the Falcon 9:
```python
rocket_data = spacexpython.rockets.falcon9()
print(rocket_data)
```

Get information about the Falcon Heavy:
```python
rocket_data = spacexpython.rockets.falconHeavy()
print(rocket_data)
```

Get information about the Big Falcon Rocket:
```python
rocket_data = spacexpython.rockets.bfr()
print(rocket_data)
```