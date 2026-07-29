import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
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
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
                {
                    "last_name": "Brown",
                    "full_name": "Olof Brown"
                }
            ],
            [
                {
                    "first_name": "Bob",
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
                {
                    "first_name": "Olof",
                    "last_name": "Brown",
                    "full_name": "Olof Brown"
                }
            ]
        )
    ]
)
def test_restore_names(users: dict, expected: dict) -> None:
    restore_names(users)
    assert users == expected
