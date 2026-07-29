from typing import List, Dict
import pytest
from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    """Test restoring first_name when missing or set to None."""
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    assert users == expected


def test_restore_names_no_missing() -> None:
    """Test when no first_name values are missing."""
    users = [
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    original_users = users.copy()

    restore_names(users)

    assert users == original_users  # Should remain unchanged


def test_restore_names_partial_data() -> None:
    """Test restoring first_name when only full_name is provided."""
    users = [
        {"first_name": None, "full_name": "Alice"},
        {"first_name": "Bob", "full_name": "Bob Brown"},
    ]
    restore_names(users)

    expected = [
        {"first_name": "Alice", "full_name": "Alice"},
        {"first_name": "Bob", "full_name": "Bob Brown"},
    ]

    assert users == expected


def test_restore_names_edge_cases() -> None:
    """Test cases with empty or space-only full_name fields."""
    users = [
        {"first_name": None, "last_name": None, "full_name": "Eve"},
        {"first_name": "", "last_name": "Taylor", "full_name": "Emma Taylor"},
        {"first_name": None, "full_name": " "},  # Edge case with just a space
    ]
    restore_names(users)

    expected = [
        {"first_name": "Eve", "last_name": None, "full_name": "Eve"},
        {"first_name": "Emma", "last_name": "Taylor",
         "full_name": "Emma Taylor"},
        {"first_name": None, "full_name": " "},  # Should remain None
    ]

    assert users == expected


def test_restore_names_empty_list() -> None:
    """Test function behavior with an empty list."""
    users: List[Dict[str, str]] = []

    restore_names(users)

    assert users == []  # Should remain an empty list


def test_restore_names_invalid_full_name() -> None:
    """Test when full_name is empty or contains only spaces."""
    users = [
        {"first_name": None, "full_name": ""},
        {"first_name": None, "full_name": "   "},  # Only spaces
    ]
    restore_names(users)

    expected = [
        {"first_name": None, "full_name": ""},
        {"first_name": None, "full_name": "   "},
    ]

    assert users == expected  # Should remain unchanged as full_name is empty


if __name__ == "__main__":
    pytest.main()
