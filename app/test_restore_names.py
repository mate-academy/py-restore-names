import pytest
from app.restore_names import restore_names


def test_first_name_is_none():
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    result = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(user)
    assert user == result


def test_first_name_is_missing():
    user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    result = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(user)
    assert user == result
