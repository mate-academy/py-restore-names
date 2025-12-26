import pytest
from app.restore_names import restore_names
from typing import List, Dict, Any


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [{
                "first_name": None,
                "last_name": "Smith",
                "full_name": "John Smith"
            }],
            ["John"],
        ),
        ([{"last_name": "Adams", "full_name": "Mike Adams"}], ["Mike"]),
        (
            [
                {
                    "first_name": "Alice",
                    "last_name": "Wonder",
                    "full_name": "Alice Wonder",
                }
            ],
            ["Alice"],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {"last_name": "Adams", "full_name": "Mike Adams"},
                {
                    "first_name": "Eva",
                    "last_name": "Brown",
                    "full_name": "Eva Brown"
                },
            ],
            ["Jack", "Mike", "Eva"],
        ),
    ],
)
def test_restore_names(
    users: List[Dict[str, Any]], expected_first_names: List[str]
) -> None:
    result = restore_names(users)
    assert result is None
    for user, expected_first in zip(users, expected_first_names):
        assert user["first_name"] == expected_first
