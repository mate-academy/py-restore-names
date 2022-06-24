import pytest
from app.restore_names import restore_names


@pytest.fixture()
def temp_user():
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_first_name_is_none(temp_user):
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    assert restore_names(user) == temp_user


def test_when_user_have_not_first_name(temp_user):
    user = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    assert restore_names(user) == temp_user
