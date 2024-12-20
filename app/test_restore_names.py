import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_exaple() -> dict:
    users = [
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

    return users


def test_user_with_none(users: dict) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_user_with_empty_name(users: dict) -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
