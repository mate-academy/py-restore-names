import pytest
from unittest import mock
from app.restore_names import restore_names


def test_first_name_is_none() -> None:
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
    expected = [
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
    restore_names(users)
    assert users == expected


def test_without_first_name() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    expected = [
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
    restore_names(users)
    assert users == expected
