import pytest
from app.restore_names import restore_names


def test_restore_first_name_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Anna Smith"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        },
    ]


def test_restore_first_name_when_missing() -> None:
    users = [
        {
            "last_name": "AdAMS",
            "full_name": "Mike Adams"
        },
        {
            "last_name": "Johnson",
            "full_name": "Emma Johnson"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "AdAMS",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Emma",
            "last_name": "Johnson",
            "full_name": "Emma Johnson"
        },
    ]


def test_do_not_change_first_name_if_exists() -> None:
    users = [
        {
            "first_name": "Tom",
            "last_name": "Riddle",
            "full_name": "Tom Riddle"
        },
        {
            "first_name": "Harry",
            "last_name": "Potter",
            "full_name": "Harry Potter"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Tom",
            "last_name": "Riddle",
            "full_name": "Tom Riddle"
        },
        {
            "first_name": "Harry",
            "last_name": "Potter",
            "full_name": "Harry Potter"
        },
    ]


def test_handle_full_name_with_more_than_two_words() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Michael Doe"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Michael Doe"
        },
    ]


def test_handle_missing_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Unknown", "full_name": ""},
    ]
    with pytest.raises(IndexError):
        restore_names(users)
