from typing import Any

from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users: list[dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_none_first_name() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_do_not_change_existing_first_name() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Jack Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_returns_none() -> None:
    users: list[dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    result = restore_names(users)

    assert result is None
