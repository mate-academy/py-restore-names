from typing import Any

from app import restore_names


def test_restore_first_name_when_none() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_when_missing() -> None:
    users: list[dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_do_not_overwrite_existing_first_name() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Jack Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_multiple_users() -> None:
    users: list[dict[str, Any]] = [
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


def test_empty_users_list() -> None:
    users: list[dict[str, Any]] = []

    result = restore_names(users)

    assert users == []
    assert result is None


def test_function_returns_none() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": None,
            "full_name": "Jack Holy",
        }
    ]

    assert restore_names(users) is None


def test_existing_empty_string_is_not_overwritten() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": "",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == ""
