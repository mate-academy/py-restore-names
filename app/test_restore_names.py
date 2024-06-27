import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": None, "last_name": "Adams",
                 "full_name": "Mike Adams"}
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"}
            ]
        ),
        (
            [
                {"first_name": "Alice", "last_name": "Wonderland",
                 "full_name": "Alice Wonderland"},
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            [
                {"first_name": "Alice", "last_name": "Wonderland",
                 "full_name": "Alice Wonderland"},
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ]
        ),
        (
            [
                {"first_name": "Alice", "last_name": "Wonderland",
                 "full_name": "Alice Wonderland"},
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            [
                {"first_name": "Alice", "last_name": "Wonderland",
                 "full_name": "Alice Wonderland"},
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ]
        ),
        (
            [
                {"last_name": "Adams",
                 "full_name": "Mike Adams"},
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            [
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ]
        ),
        (
            [],
            []
        )
    ]
)
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
