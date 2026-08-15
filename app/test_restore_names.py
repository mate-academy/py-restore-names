from app.restore_names import restore_names
from typing import List, Dict, Any


def test_restore_names_first_name_none() -> None:
    """Test that first_name is restored when it is None."""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_first_name_missing() -> None:
    """Test that first_name is restored when it is missing."""
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_first_name_exists() -> None:
    """Test that first_name is not changed if it already exists."""
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_multiple_users() -> None:
    """Test that first_name is restored for multiple users."""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "John"


def test_restore_names_full_name_single_word() -> None:
    """Test that first_name is restored when full_name has only one word."""
    users = [
        {
            "first_name": None,
            "last_name": None,
            "full_name": "Madonna",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Madonna"


def test_restore_names_empty_list() -> None:
    """Test that function works with an empty list of users."""
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []
