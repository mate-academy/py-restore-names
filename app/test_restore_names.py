import pytest
from app.restore_names import restore_names


# write your tests here
@pytest.fixture()
def user_template() -> list:
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
    yield users
    del users


def test_restores_missing_or_broken_names(user_template: callable) -> None:
    users = user_template
    restore_names(user_template)
    for user in users:
        assert user.get("first_name") == user.get("full_name").split()[0]
