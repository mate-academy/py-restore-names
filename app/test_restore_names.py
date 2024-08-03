import pytest
from app.restore_names import restore_names


@pytest.fixture
def get_users() -> list[dict]:
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


def test_fixing_first_name_none(get_users: list[dict]) -> None:
    users = get_users
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_fixing_no_first_name(get_users: list[dict]) -> None:
    users = get_users
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
