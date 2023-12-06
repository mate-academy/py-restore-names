import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_not_restored() -> list[dict]:
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


@pytest.fixture()
def user_restored() -> list[dict]:
    users = [
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
    return users


def test_first_name_is_none(users_not_restored: list[dict],
                            user_restored: list[dict]) -> None:
    restore_names(users_not_restored)
    assert users_not_restored == user_restored


def test_first_name_is_not_exist(users_not_restored: list[dict],
                                 user_restored: list[dict]) -> None:
    restore_names(users_not_restored)
    assert users_not_restored == user_restored
