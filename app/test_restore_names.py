from typing import List, Dict
from app.restore_names import restore_names


def test_restore_names_restores_missing_first_name() -> None:
    users: List[Dict[str, str | None]] = [
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


def test_restore_names_keeps_existing_first_name() -> None:
    users: List[Dict[str, str | None]] = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Anna"


def test_restore_names_handles_multiple_users() -> None:
    users: List[Dict[str, str | None]] = [
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Tom Brown",
        },
        {
            "first_name": "Eva",
            "last_name": "Stone",
            "full_name": "Eva Stone",
        },
        {
            "first_name": None,
            "last_name": "Lee",
            "full_name": "Sara Lee",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Tom"
    assert users[1]["first_name"] == "Eva"
    assert users[2]["first_name"] == "Sara"


def test_restore_names_ignores_users_without_full_name() -> None:
    users: List[Dict[str, str | None]] = [
        {
            "first_name": None,
            "last_name": "X",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] is None
