import pytest
from app.restore_names import restore_names


def test_restore_names_user_is_none():
    users = (
        [{"first_name": None,
          "last_name": "Daniels",
          "full_name": "Jack Daniels"}])

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_names_not_name():
    users = (
        [{"last_name": "Walker",
          "full_name": "Johnie Walker"}])

    restore_names(users)

    assert users[0]["first_name"] == "Johnie"
