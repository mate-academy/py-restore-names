import pytest
from app.restore_names import restore_names
from typing import Callable


@pytest.fixture()
def first_user() -> list[dict]:
    return [{
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


def test_first_name_is_not_in_user(first_user: Callable) -> None:
    restore_names(first_user)
    assert first_user == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


def test_first_name_equals_none(first_user: Callable) -> None:
    first_user[0]["first_name"] = None
    restore_names(first_user)
    assert first_user == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
