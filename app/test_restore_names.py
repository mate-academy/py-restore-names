import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        pytest.param(
            [
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ],
            [
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ]
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ],
            [
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ]
        ),
        pytest.param(
            [
                {
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ],
            [
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ]
        ),
        pytest.param(
            [
                {
                    "last_name": "lname",
                    "full_name": "fname lname"
                },
                {
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ],
            [
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                },
                {
                    "first_name": "fname",
                    "last_name": "lname",
                    "full_name": "fname lname"
                }
            ]
        ),
    ]
)
def test_restore_names(users: dict, expected_users: str) -> None:
    restore_names(users)
    assert users == expected_users
