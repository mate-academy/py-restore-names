import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def users() -> list:
    return [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_if_user_name_not_in_user(users: list) -> None:
    for user in users:
        if "first_name" not in user:
            assert restore_names(users) == user["first_name"]


def test_if_user_name_already_in_user(users: list) -> None:
    for user in users:
        if user["first_name"] is None:
            assert restore_names(users) == user["first_name"]
