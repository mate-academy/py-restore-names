import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return users


def test_when_first_name_equal_none(users_template):
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_when_field_first_name_is_lost(users_template):
    restore_names(users_template)
    assert users_template[1]["first_name"] == "Mike"
