import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }]
        ),
        (
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }]
        )
    ],
    ids=[
        "check if 'first_name' is None",
        "check if 'first_name' key is not exists"
    ]
)
def test_restore_names(users: list, expected_users: list) -> None:
    restore_names(users)
    assert users == expected_users
