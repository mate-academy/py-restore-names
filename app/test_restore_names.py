import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected",
    [
        (
                {  # noqa
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",  # noqa
                },
        ),
        (
                { # noqa
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
        )
    ]
)
def test_restore_first_name_or_last_name_if_that_not_exist(user, expected):  # noqa
    list_users_dict = [user]
    restore_names(list_users_dict)
    assert list_users_dict[0] == expected
