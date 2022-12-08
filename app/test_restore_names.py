import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return users


def test_function_returns_nothing(user_template):
    assert restore_names(user_template) is None


def test_function_works_correctly(user_template):
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
    assert user_template[1]["first_name"] == "Mike"
