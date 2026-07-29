import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            }
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            }
        ]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "Alice Smith",
            }
        ],
        [
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "full_name": "Alice Smith",
            }
        ]
    ),
    (
        [
            {
                "last_name": "Brown",
                "full_name": "Emily Brown",
            }
        ],
        [
            {
                "first_name": "Emily",
                "last_name": "Brown",
                "full_name": "Emily Brown",
            }
        ]
    ),
    (
        [
            {
                "first_name": "Peter",
                "last_name": "Parker",
                "full_name": "Peter Parker",
            },
            {
                "first_name": None,
                "last_name": "Johnson",
                "full_name": "Bruce Johnson",
            },
            {
                "last_name": "Davis",
                "full_name": "Jessica Davis",
            }
        ],
        [
            {
                "first_name": "Peter",
                "last_name": "Parker",
                "full_name": "Peter Parker",
            },
            {
                "first_name": "Bruce",
                "last_name": "Johnson",
                "full_name": "Bruce Johnson",
            },
            {
                "first_name": "Jessica",
                "last_name": "Davis",
                "full_name": "Jessica Davis",
            }
        ]
    ),
    ([], [])
])
def test_restore_names(
        input_users: list[dict],
        expected_users: list[dict]
) -> None:

    restore_names(input_users)
    assert input_users == expected_users
