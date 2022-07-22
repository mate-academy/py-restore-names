import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users():
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


def test_first_name_is_none(users):
    restore_names([users[0]])

    assert [users[0]] == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_first_name_not_existing(users):
    restore_names([users[1]])

    assert [users[1]] == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
