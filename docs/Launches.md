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