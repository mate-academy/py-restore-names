import pytest

from app.restore_names import restore_names
from typing import List


@pytest.fixture
def users_list() -> List[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


@pytest.fixture
def expected_users() -> List[dict]:
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


def test_only_when_first_name_is_none(
        users_list: List[dict],
        expected_users: List[dict]
) -> None:
    users_list[0]["first_name"] = users_list[0]["first_name"] = None
    restore_names(users_list)
    assert users_list == expected_users


def test_only_when_first_name_is_missing(
        users_list: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(users_list)
    assert users_list == expected_users
