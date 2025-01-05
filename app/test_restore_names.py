from typing import List

import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_fixture() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_restore_names(users_fixture: List[dict]) -> None:
    users = users_fixture
    restore_names(users)
    assert users == [
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


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_no_full_name() -> None:
    users = [{"first_name": "Jack"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
