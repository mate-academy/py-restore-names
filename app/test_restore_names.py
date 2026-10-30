import pytest
from app.main import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Jack Smith",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Jack Smith",
        }
    ]


def test_restore_names_for_multiple_users() -> None:
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

    restore_names(users)

    assert users == [
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
