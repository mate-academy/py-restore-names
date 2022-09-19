import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_list():
    return [
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


def test_restore_only_missing_names(users_list):
    for user in users_list:
        if "first_name" not in user:
            restore_names([user])
            assert user["first_name"] == user["full_name"].split()[0]


def test_restore_only_none_names(users_list):
    for user in users_list:
        if "first_name" in user and user["first_name"] is None:
            restore_names([user])
            assert user["first_name"] == user["full_name"].split()[0]
