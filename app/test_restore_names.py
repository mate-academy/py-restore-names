import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_name():
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


def test_if_first_name_is_none(users_name):
    restore_names([users_name[0]])
    assert [users_name[0]] == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_if_first_name_not_in_key(users_name):
    restore_names([users_name[1]])
    assert [users_name[1]] == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
