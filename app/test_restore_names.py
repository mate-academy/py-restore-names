import pytest
from copy import deepcopy

from app.restore_names import restore_names


@pytest.fixture(scope="module")
def valid_users() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


@pytest.fixture()
def users(valid_users: list[dict]) -> list[dict]:
    return deepcopy(valid_users)


def test_restore_names_if_names_present(
    users: list[dict],
    valid_users: list[dict]
) -> None:
    restore_names(users)
    assert users == valid_users


def test_restore_names_if_names_is_not_present(
    users: list[dict],
    valid_users: list[dict]
) -> None:
    for user in users:
        user.pop("first_name")
    restore_names(users)
    assert users == valid_users


def test_restore_names_if_names_are_none(
    users: list[dict],
    valid_users: list[dict]
) -> None:
    for user in users:
        user["first_name"] = None
    restore_names(users)
    assert users == valid_users
