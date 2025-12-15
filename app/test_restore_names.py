import pytest
from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def users() -> List[dict]:
    return [
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


def test_if_first_name_is_none(users: List[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_if_no_key_first_name(users: List[dict]) -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
