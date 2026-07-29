import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            id="When first name is `None`"
        ),
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }],
            id="When dict not exist `first_name` key"
        )
    ]
)
def test_restore_names(users: list[dict], expected_users: list[dict]) -> None:
    restore_names(users)
    assert users == expected_users
