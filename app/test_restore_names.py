import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


def test_restore_name_with_user_firstname_is_none(user):
    restore_names(user)

    assert user[0]["first_name"] == "Jack"


def test_restore_name_with_user_firstname_is_missing(user):
    restore_names(user)

    assert user[0]["first_name"]
