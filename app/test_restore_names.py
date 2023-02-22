import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mark",
            "last_name": "Black",
            "full_name": "Mark Black",
        }
    ]
    return users


def test_first_name_if_it_does_not_exist(users):
    restore_names(users)
    assert "first_name" in users[0]


def test_first_name_if_it_is_none(users):
    restore_names(users)
    assert users[1]["first_name"] == "Jack"


def test_first_name_if_it_has_a_name(users):
    restore_names(users)
    assert users[2]["first_name"] == users[2]["full_name"].split()[0]
