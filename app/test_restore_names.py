import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        [
            [
                {"first_name": None,
                 "last_name": "Holy", "full_name": "Jack Holy"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
            ],
        ]
    ],
)
def test_update_of_none_or_missing_value(users, expected_users):
    restore_names(users)
    assert users == expected_users
