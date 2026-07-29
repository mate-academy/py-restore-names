import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_params() -> list:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},

        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    yield users


def test_restore_names(user_params: list) -> None:
    expected_users = [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},

        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(user_params)
    assert user_params == expected_users
