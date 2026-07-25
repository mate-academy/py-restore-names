from typing import List

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users() -> List[dict]:
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


def test_base_names_restoring(users: list[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_one_letter_names_restoring(users: list[dict]) -> None:
    users[0]["full_name"] = "S Pul"
    restore_names(users)
    assert users[0]["first_name"] == "S"


def test_empty_names_restoring(users: list[dict]) -> None:
    users[0]["full_name"] = "_ _"
    restore_names(users)
    assert users[0]["first_name"] == "_"
