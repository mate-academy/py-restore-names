import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template():
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


def test_first_name_is_none(user_template):
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_first_name_is_lost(user_template):
    restore_names(user_template)
    assert user_template[1]["first_name"] == "Mike"
