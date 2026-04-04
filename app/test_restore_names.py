from typing import List, Dict, Any
from app.restore_names import restore_names


def test_restore_when_first_name_none() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_missing() -> None:
    users: List[Dict[str, Any]] = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_override_existing_first_name() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": "John", "last_name": "Smith", "full_name": "Jack Smith"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_multiple_users() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "full_name": "Alice Cooper"},
        {"full_name": "Bob Marley"},
        {"first_name": "Charlie", "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"


def test_function_returns_none() -> None:
    users: List[Dict[str, Any]] = [{"full_name": "Test User"}]
    result = restore_names(users)
    assert result is None


def test_full_name_single_word() -> None:
    users: List[Dict[str, Any]] = [{"first_name": None, "full_name": "Madonna"}]
    restore_names(users)
    assert users[0]["first_name"] == "Madonna"
