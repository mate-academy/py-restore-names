import pytest
from typing import Any
from app.restore_names import restore_names


@pytest.fixture()
def users_fixture() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Adam",
            "last_name": "Savage",
            "full_name": "Adam Savage"
        },
        {
            "last_name": "Parker",
            "full_name": "Peter Parker"
        }
    ]


def test_restore_names(users_fixture: Any) -> None:
    restore_names(users_fixture)
    assert users_fixture == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Adam",
            "last_name": "Savage",
            "full_name": "Adam Savage"
        },
        {
            "first_name": "Peter",
            "last_name": "Parker",
            "full_name": "Peter Parker"
        }
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
