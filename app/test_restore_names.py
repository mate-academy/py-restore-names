from app.restore_names import restore_names
from typing import Any


def test_restore_name_none() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Alice Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_name_missing() -> None:
    users = [
        {
            "last_name": "Brown",
            "full_name": "Tom Brown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"


def test_no_change_if_name_present() -> None:
    users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_multiple_users() -> None:
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
            "first_name": "Anna",
            "last_name": "White",
            "full_name": "Anna White",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"
