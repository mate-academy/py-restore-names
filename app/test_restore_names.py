import pytest
from app.restore_names import restore_names

# write your tests here
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

def test_restore_names():
    restore_names(users)
    assert users == [
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