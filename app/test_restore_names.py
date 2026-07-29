import pytest  # noqa: F401
from app.restore_names import restore_names


def test_if_first_name_is_none() -> None:
    testing_users_1 = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    },

        {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    },]

    restore_names(testing_users_1)
    for user in testing_users_1:
        assert user["first_name"] is not None


def test_if_users_is_empty() -> None:
    testing_users_2 = []
    restore_names(testing_users_2)
    assert testing_users_2 == []
