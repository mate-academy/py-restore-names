from typing import List, Dict, Optional
from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_without_first_name_key() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_existing_first_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_single_word_full_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack"},
        {"last_name": "Adams", "full_name": "Mike"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
