import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template():
    return [
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


def test_users_are_restored(user_template) -> None:
    users_restored = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(user_template)
    assert users_restored == user_template
