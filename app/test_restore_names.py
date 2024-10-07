import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            id=("Test when 'first_name' is None, "
                "it should restore from 'full_name'"
                )
        ),
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            id=("Test when 'first_name' doesn't exist, "
                "it should restore from 'full_name'"
                )
        )
    ]
)
def test_should_(users: [dict], expected_users: [dict]) -> None:
    restore_names(users)
    assert users == expected_users
