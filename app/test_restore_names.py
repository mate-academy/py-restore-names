import pytest
from .restore_names import restore_names
from typing import List


@pytest.fixture()
def users() -> List[dict]:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"}
    ]


def test_restore_names(users: List[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"
