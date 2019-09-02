Get all capsule information:
```python
capsules = spacexpython.capsules()
print(capsule)
```

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