from typing import List, Dict, Any
from app.restore_names import restore_names


def test_existing_first_name_not_changed() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": "John", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Alice", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    first_names = [user["first_name"] for user in users]
    assert first_names == ["John", "Alice"]


def test_full_name_with_multiple_words() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "last_name": "Doe",
         "full_name": "Mary Jane Doe"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mary"


def test_empty_users_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []
