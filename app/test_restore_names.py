import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_input() -> list:
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
    return users


@pytest.fixture
def expected_users() -> list:
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return expected


def test_restore_names(user_input: list, expected_users: list) -> None:
    restore_names(user_input)
    assert user_input == expected_users
