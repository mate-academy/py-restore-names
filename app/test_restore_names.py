from typing import List, Dict
from app.restore_names import restore_names


# 🧪 Test suite with annotations


def test_restore_names_none_first_name() -> None:
    users: List[Dict[str, str | None]] = [
        {"first_name": None, "last_name": "Smith", "full_name": "Alice Smith"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_names_missing_first_name() -> None:
    users: List[Dict[str, str | None]] = [
        {"last_name": "Brown", "full_name": "Charlie Brown"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Charlie"


def test_restore_names_valid_first_name() -> None:
    users: List[Dict[str, str | None]] = [
        {
            "first_name": "Emily",
            "last_name": "Stone",
            "full_name": "Emily Stone"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"  # unchanged


def test_restore_names_multiple_users() -> None:
    users: List[Dict[str, str | None]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Susan",
            "last_name": "Clark",
            "full_name": "Susan Clark"
        }
    ]
    restore_names(users)
    expected: List[str] = ["Jack", "Mike", "Susan"]
    actual: List[str | None] = [u["first_name"] for u in users]
    assert actual == expected
