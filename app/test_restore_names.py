from typing import List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ],
        [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "full_name": "Alice Smith"
            },
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "full_name": "Alice Smith"
            },
        ]
    ),
])
def test_restore_names(input_users: List[dict], expected_users: dict) -> None:
    # Call the restore_names function
    restore_names(input_users)

    # Assert that the first names have been restored correctly
    assert input_users == expected_users
