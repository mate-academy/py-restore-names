import pytest
from app.restore_names import restore_names


def test_restore_names():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Emily", "last_name": "Clark", "full_name": "Emily Clark"},
    ]

    restore_names(users)

    expected_users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Emily", "last_name": "Clark", "full_name": "Emily Clark"},
    ]

    assert users == expected_users


def test_no_change_when_first_name_present():
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]

    restore_names(users)

    expected_users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]

    assert users == expected_users


def test_ignore_missing_full_name():
    users = [
        {"first_name": None, "last_name": "Holy"},
        {"first_name": None, "last_name": "Doe"},
    ]

    restore_names(users)

    expected_users = [
        {"first_name": None, "last_name": "Holy"},
        {"first_name": None, "last_name": "Doe"},
    ]

    assert users == expected_users


def test_partial_full_name():
    users = [
        {"first_name": None, "full_name": "Anna"},
        {"first_name": None, "full_name": "Bob Marley"},
    ]

    restore_names(users)

    expected_users = [
        {"first_name": "Anna", "full_name": "Anna"},
        {"first_name": "Bob", "full_name": "Bob Marley"},
    ]

    assert users == expected_users


def test_empty_list():
    users = []

    restore_names(users)

    expected_users = []

    assert users == expected_users
