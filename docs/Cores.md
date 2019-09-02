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