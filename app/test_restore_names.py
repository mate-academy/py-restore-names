import pytest
from app.restore_names import restore_names


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def restore_names_without_spaces() -> None:
    users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restoring_missing_first_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
