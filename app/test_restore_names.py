import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
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
                }
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
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith"
                },
                {
                    "first_name": None,
                    "last_name": "Doe",
                    "full_name": "John Doe"
                }
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Brown",
                    "full_name": "Charlie Brown"
                },
                {
                    "first_name": None,
                    "last_name": "Johnson",
                    "full_name": "Eli Johnson"
                }
            ],
            [
                {
                    "first_name": "Charlie",
                    "last_name": "Brown",
                    "full_name": "Charlie Brown"
                },
                {
                    "first_name": "Eli",
                    "last_name": "Johnson",
                    "full_name": "Eli Johnson"
                }
            ]
        ),
    ]
)
def test_restore_names(users: list, expected: list) -> None:
    restore_names(users)
    assert users == expected
