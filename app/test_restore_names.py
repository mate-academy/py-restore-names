from typing import List, Dict
from app.restore_names import restore_names


def test_restore_names_sets_first_name_when_missing() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_names_does_not_change_existing_first_name() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]


def test_restore_names_handles_missing_full_name() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": None, "last_name": "Holy"},
        {"first_name": None, "last_name": "Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": None, "last_name": "Holy"},
        {"first_name": None, "last_name": "Doe"},
    ]


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, str]] = []
    restore_names(users)
    assert users == []


def test_restore_names_sets_first_name_when_missing_key() -> None:
    users: List[Dict[str, str]] = [
        {"last_name": "Smith", "full_name": "Alice Smith"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice",
         "last_name": "Smith", "full_name": "Alice Smith"},
    ]


def test_restore_names_sets_first_when_full_name_has_single_name() -> None:
    users: List[Dict[str, str]] = [
        {"first_name": None, "full_name": "Anna"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Anna", "full_name": "Anna"},
    ]
