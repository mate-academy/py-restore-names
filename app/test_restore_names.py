import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize("users, expected_names", [
    (
        [{"full_name": "John Doe", "first_name": None},
         {"full_name": "Alice Smith"},
         {"full_name": "Bob Johnson", "first_name": "Bob"}],
        ["John", "Alice", "Bob"]
    ),
    (
        [{"full_name": "Jane Smith", "first_name": "Jane"},
         {"full_name": "Michael Brown", "first_name": None},
         {"full_name": "Emily Davis", "first_name": "Emily"}],
        ["Jane", "Michael", "Emily"]
    ),
])
def test_restore_names(users: List[Dict[str, str]], expected_names: List[str]):
    restore_names(users)

    for user, expected_name in zip(users, expected_names):
        assert user["first_name"] == expected_name


@pytest.mark.parametrize("users", [
    [{"full_name": "John Doe", "first_name": "John"},
     {"full_name": "Alice Smith", "first_name": "Alice"},
     {"full_name": "Bob Johnson", "first_name": "Bob"}],
    [{"full_name": "Jane Smith", "first_name": "Jane"},
     {"full_name": "Michael Brown", "first_name": "Michael"},
     {"full_name": "Emily Davis", "first_name": "Emily"}],
])
def test_restore_names_no_changes(users: List[Dict[str, str]]):
    original_users = users.copy()
    restore_names(users)

    assert users == original_users
