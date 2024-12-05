import pytest
from app.restore_names import restore_names


def test_no_change_if_first_name_exists() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Smith", "full_name":
            "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    expected_users = users.copy()
    restore_names(users)
    assert users == expected_users


def test_empty_user_list() -> None:
    users = []
    restore_names(users)
    assert users == []
