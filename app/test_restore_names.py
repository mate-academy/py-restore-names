from typing import Any
from app.restore_names import restore_names


def test_restore_names_sets_first_name_when_value_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_sets_first_name_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_does_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Mike Smith",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Mike Smith",
        }
    ]


def test_restore_names_handles_multiple_users() -> Any:
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
        {
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
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
        {
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        },
    ]
