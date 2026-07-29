import pytest
from typing import List, Dict, Optional
from app.restore_names import restore_names


def test_restore_none_first_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_keep_valid_first_name() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": "Alice", "last_name": "Doe", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_empty_users_list() -> None:
    users: List[Dict[str, str]] = []
    restore_names(users)
    assert users == []


@pytest.mark.parametrize("full_name, expected", [
    ("", None),
    (None, None),
    ("SingleName", "SingleName"),
])
def test_invalid_full_name_behavior(
        full_name: Optional[str],
        expected: Optional[str]
) -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Smith", "full_name": full_name}
    ]
    restore_names(users)
    assert users[0].get("first_name") == expected


def test_multiple_users_restore() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {
            "first_name": None,
            "last_name": "One",
            "full_name": "First One",
        },
        {
            "first_name": "Already",
            "last_name": "Two",
            "full_name": "Second Two",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "First"
    assert users[1]["first_name"] == "Already"


def test_first_name() -> None:
    users: List[Dict[str, str]] = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
