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
                "full_name": "Mike Adams"}
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
            }
        ]
    ),
    (
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "Jane Smith"
            }
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "full_name": "Jane Smith"
            }
        ]
    ),
    (
        [
            {
                "last_name": "Johnson",
                "full_name": "Robert Johnson"
            },
            {
                "first_name": "Emily",
                "last_name": "Williams",
                "full_name": "Emily Williams"
            }
        ],
        [
            {
                "first_name": "Robert",
                "last_name": "Johnson",
                "full_name": "Robert Johnson"
            },
            {
                "first_name": "Emily",
                "last_name": "Williams",
                "full_name": "Emily Williams"
            }
        ]
    ),
])
def test_restore_names(
        input_users: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
