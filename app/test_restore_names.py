import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": None,
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
            ],
            id="should restore missing first name"
        )
    ]
)
def test_restore_first_name(users: dict, expected_users: dict) -> None:
    restore_names(users)
    assert users == expected_users
