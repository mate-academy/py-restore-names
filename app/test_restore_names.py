from typing import List, Dict, Optional
from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_names_with_all_first_names_present() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John", "last_name": "Doe",
         "full_name": "John Doe"},
    ]
    expected: List[Dict[str, str]] = users.copy()
    restore_names(users)
    assert users == expected


def test_restore_names_with_empty_list() -> None:
    users: List[Dict[str, str]] = []
    restore_names(users)
    assert users == []


def test_restore_names_partial_none_and_present() -> None:
    users: List[Dict[str, Optional[str]]] = [
        {"first_name": "Alice", "last_name": "Brown",
         "full_name": "Alice Brown"},
        {"first_name": None, "last_name": "Davis",
         "full_name": "Tom Davis"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice", "last_name": "Brown",
         "full_name": "Alice Brown"},
        {"first_name": "Tom", "last_name": "Davis",
         "full_name": "Tom Davis"},
    ]


def test_restore_names_not_returning_anything() -> None:
    users: List[Dict[str, Optional[str]]] = [{
        "first_name": None,
        "last_name": "Lee",
        "full_name": "Sam Lee"
    }]
    result = restore_names(users)
    assert result is None
