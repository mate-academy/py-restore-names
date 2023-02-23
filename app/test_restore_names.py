import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_input() -> list:
    user = [
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
    return user


@pytest.fixture()
def users_output() -> list:
    user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return user


def test_restore_names(users_input, users_output) -> None:
    restore_names(users_input)
    assert users_input == users_output
