from typing import List, Dict, Any
from app import restore_names


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_should_not_touch_existing_first_name() -> None:
    users = [
        {
            "first_name": "Alex",
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Alex",
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]


def test_empty_users_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names.restore_names(users)
    assert users == []
