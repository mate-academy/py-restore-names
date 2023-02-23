import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, restored_name",
    [
        (
            [
                {
                    "first_name": "Jasmine",
                    "last_name": "Patel",
                    "full_name": "Jasmine Patel"
                }
            ],
            [
                {
                    "first_name": "Jasmine",
                    "last_name": "Patel",
                    "full_name": "Jasmine Patel"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Ramirez",
                    "full_name": "Xavier Ramirez"
                }
            ],
            [
                {
                    "first_name": "Xavier",
                    "last_name": "Ramirez",
                    "full_name": "Xavier Ramirez"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Giga",
                    "full_name": "Jasmine Patel"
                },
                {
                    "first_name": None,
                    "last_name": "Ramirez",
                    "full_name": "Xavier Ramirez"
                }
            ],
            [
                {
                    "first_name": "Jasmine",
                    "last_name": "Patel",
                    "full_name": "Jasmine Patel"
                },
                {
                    "first_name": "Xavier",
                    "last_name": "Ramirez",
                    "full_name": "Xavier Ramirez"
                }
            ]
        ),
        ([], [])
    ]
)
def test_restore_names(users, restored_name):
    restore_names(users)
    assert users == restored_name, (
        "Function should return 'first_name' for users in given list"
    )
