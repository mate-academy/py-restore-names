import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
        ),
    ],
)
def test_restore_names(users: list, expected_users: list) -> None:
    restore_names(users)
    assert users == expected_users


def test_restore_names_should_return_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
