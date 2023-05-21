import pytest
from app.restore_names import restore_names

@pytest.fixture()
def user_template() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_first_name_key_doesnt_exist(user_template) -> None:
    user = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",  
        }
    ]
    restore_names(user)
    assert user == user_template


def test_first_name_value_none(user_template) -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",  
        }
    ]
    restore_names(user)
    assert user == user_template


def test_first_name_exists(user_template) -> None:
    user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",  
        }
    ]
    restore_names(user)
    assert user == user_template