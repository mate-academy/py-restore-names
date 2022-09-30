import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        pytest.param(
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            id="if first_name is None , take name from full_name"
        ),
        pytest.param(
            {"last_name": "Adams",
             "full_name": "Mike Adams"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"},
            id="if first_name is empty, create it and take name in full_name"
        )
    ]
)
def test_restore_name(users, expected_users):
    assert restore_names(users) == expected_users
