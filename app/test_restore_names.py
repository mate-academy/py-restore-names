from typing import List, Dict
from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users: List[Dict] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_missing() -> None:
    users: List[Dict] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_should_not_override_existing_first_name() -> None:
    users: List[Dict] = [
        {
            "first_name": "Johnny",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Johnny"


def test_restore_names_with_empty_list() -> None:
    users: List[Dict] = []
    restore_names(users)
    assert users == []


def test_restore_names_complex_list() -> None:
    users: List[Dict] = [
        {"full_name": "Alice Cooper"},
        {"first_name": None, "full_name": "Bob Marley"},
        {"first_name": "Charlie", "full_name": "Chuck Norris"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"
