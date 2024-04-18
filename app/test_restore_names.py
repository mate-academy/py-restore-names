import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def create_users_list() -> list[dict]:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    yield users
    del users


def test_restore_only_none_names(create_users_list: list[dict]) -> None:
    users = create_users_list
    restore_names(users)
    assert users[0].get("first_name") == "Jack"


def test_restore_only_missing_names(create_users_list: list[dict]) -> None:
    users = create_users_list
    del users[0]["first_name"]
    restore_names(users)
    assert users[0].get("first_name", False) == "Jack"
