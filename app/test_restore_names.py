import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_users, expected_users",
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
            ],
        ),
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                }
            ],
            [
                {"first_name": "John",
                 "last_name": "Doe",
                 "full_name": "John Doe"
                 }
            ],
        ),
        (
            [
                {
                    "last_name": "OneName",
                    "full_name": "SingleName"
                }
            ],
            [
                {
                    "first_name": "SingleName",
                    "last_name": "OneName",
                    "full_name": "SingleName"
                }
            ],
        ),
        (
            [
                {"first_name": None,
                 "last_name": "DoubleFirst",
                 "full_name": "Double First Name"
                 }
            ],
            [
                {
                    "first_name": "Double",
                    "last_name": "DoubleFirst",
                    "full_name": "Double First Name"
                }
            ],
        ),
    ],
)
def test_restore_names(initial_users: [dict],
                       expected_users: [dict]) -> None:
    users_to_restore = [user.copy() for user in initial_users]
    restore_names(users_to_restore)
    assert users_to_restore == expected_users
