from app.restore_names import restore_names

# write your tests here
from typing import List, Dict
import pytest


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ]
        ),
        (
            [
                {"first_name": "John", "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": None, "last_name": "Smith",
                 "full_name": "Alice Smith"},
            ],
            [
                {"first_name": "John", "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": "Alice", "last_name": "Smith",
                 "full_name": "Alice Smith"},
            ]
        ),
        (
            [
                {"last_name": "Brown",
                 "full_name": "Charlie Brown"},
            ],
            [
                {"first_name": "Charlie", "last_name": "Brown",
                 "full_name": "Charlie Brown"},
            ]
        ),
    ]
)
def test_restore_names(users: List[Dict], expected: List[Dict]) -> None:
    """Test that restore_names correctly restores first_name."""
    restore_names(users)
    assert users == expected


def test_restore_names_does_not_return_anything() -> None:
    """Function should not return anything."""
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    result = restore_names(users)
    assert result is None
