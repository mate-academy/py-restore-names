import pytest
from app.restore_names import restore_names


def test_restore_first_name_when_none():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Smith"}
    ]
    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "John"


def test_restore_first_name_when_missing():
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_first_name_not_changed_when_present():
    users = [
        {"first_name": "Alice", "last_name": "Wonder", "full_name": "Alice Wonder"}
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Alice"


def test_multiple_users_restore():
    users = [
        {"first_name": None, "last_name": "Serhiienko", "full_name": "Vladyslav Serhiienko"},
        {"last_name": "Serzhan", "full_name": "Anna Serzhan"},
        {"first_name": "Catherine", "last_name": "X", "full_name": "Catherine X"}
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Vladyslav"
    assert users[1]["first_name"] == "Anna"
    assert users[2]["first_name"] == "Catherine"
