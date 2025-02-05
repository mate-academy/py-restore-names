import pytest
from app.restore_names import restore_names


def test_restore_names():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": None, "last_name": "Brown", "full_name": "Sarah Brown"},
    ]

    restore_names(users)

    expected_users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": "Sarah", "last_name": "Brown", "full_name": "Sarah Brown"},
    ]

    assert users == expected_users
