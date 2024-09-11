import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_users, expected_result",
    [
        (
                [{"first_name": None, "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}]
        ),
        (
                [{"full_name": "Mike Adams"}],
                [{"first_name": "Mike", "full_name": "Mike Adams"}]
        )
    ]
)
def test_restore_names(list_users, expected_result):
    users_copy = [user.copy() for user in list_users]
    restore_names(users_copy)
    assert users_copy == expected_result


