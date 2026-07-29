import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def return_user() -> List[dict]:
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


def test_should_return_first_name_if_it_none(return_user: List[dict]) -> None:
    restore_names(return_user)
    assert return_user[0]["first_name"] == "Jack"


def test_should_return_first_name_if_it_empty(return_user: List[dict]) -> None:
    restore_names(return_user)
    assert return_user[1]["first_name"] == "Mike"
