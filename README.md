# Restore names

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

The database failed. Some users lost values from the `first_name` field, but
`user` dict has a `full_name` field, so we can restore `first_name`.

Write tests for `restore_names` function, that takes a list of `users` and set
correct `first_name` to users who do not have it or is equal to `None`. You
should not return anything from the function.

Example:
```python
users = [
  {
    "first_name": None,
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]

restore_names(users)

users == [
  {
    "first_name": "Jack",
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "first_name": "Mike",
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]
```

Run `pytest app/` to check if function pass your tests.

Run `pytest --numprocesses=auto tests/` to check if your tests cover all boundary conditions
and pass task tests.
