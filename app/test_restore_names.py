import pytest
from app.restore_names import restore_names


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


def test_empty_first_name():
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_first_name_none():
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
