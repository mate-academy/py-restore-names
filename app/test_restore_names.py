import pytest
from typing import List

from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected_first_names", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }
        ],
        ["Jack"]
    ),
    (
        [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        ],
        ["Mike"]
    ),
    (
        [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            }
        ],
        ["Anna"]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Charlie Brown"
            },
            {
                "last_name": "Black",
                "full_name": "Lucy Black"
            },
            {
                "first_name": "Mark",
                "last_name": "White",
                "full_name": "Mark White"
            },
        ],
        ["Charlie", "Lucy", "Mark"]
    )
])
def test_restore_names(users: List[dict], expected_first_names: str) -> None:
    restore_names(users)

    for user, expected_first_name in zip(users, expected_first_names):
        assert user["first_name"] == expected_first_name
