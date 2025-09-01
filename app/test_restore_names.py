# tests/test_restore_names.py

import pytest
from app.main import restore_names  # ajuste o import se o caminho for diferente


def test_restore_names_with_missing_first_name():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)

    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names_with_existing_first_name():
    users = [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"first_name": "Bob", "last_name": "Brown", "full_name": "Bob Brown"},
    ]
    expected = users.copy()
    restore_names(users)

    assert users == expected  # nada deve mudar


def test_restore_names_with_empty_list():
    users = []
    restore_names(users)

    assert users == []


def test_restore_names_with_single_name_full_name():
    users = [
        {"first_name": None, "last_name": "", "full_name": "Plato"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Plato"


def test_restore_names_does_not_return_anything():
    users = [{"first_name": None, "last_name": "Lee", "full_name": "Bruce Lee"}]
    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "Bruce"
