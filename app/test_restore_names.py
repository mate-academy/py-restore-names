import pytest
from app.restore_names import restore_names


def test_restore_missing_first_name():
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_none_first_name():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": None, "last_name": "Brown", "full_name": "Chris Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": "Chris", "last_name": "Brown", "full_name": "Chris Brown"},
    ]


def test_preserve_existing_first_name():
    users = [
        {"first_name": "Emily", "last_name": "Clark", "full_name": "Emily Clark"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Emily", "last_name": "Clark", "full_name": "Emily Clark"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]


def test_mixed_cases():
    users = [
        {"first_name": None, "last_name": "Taylor", "full_name": "Alex Taylor"},
        {"first_name": "Sara", "last_name": "Lee", "full_name": "Sara Lee"},
        {"last_name": "Miller", "full_name": "Tom Miller"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alex", "last_name": "Taylor", "full_name": "Alex Taylor"},
        {"first_name": "Sara", "last_name": "Lee", "full_name": "Sara Lee"},
        {"first_name": "Tom", "last_name": "Miller", "full_name": "Tom Miller"},
    ]


def test_empty_list():
    users = []
    restore_names(users)
    assert users == []
