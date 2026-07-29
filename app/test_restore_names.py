import pytest
from typing import List

from app.restore_names import restore_names


@pytest.fixture()
def list_of_users() -> list:
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


def test_restore_names_if_name_none(list_of_users: List[dict]) -> None:
    restore_names(list_of_users)
    assert list_of_users[0]["first_name"] == "Jack"


def test_restore_names_if_lose_name(list_of_users: List[dict]) -> None:
    restore_names(list_of_users)
    assert list_of_users[1]["first_name"] == "Mike"


def test_raises_type_error_if_users_empty() -> None:
    with pytest.raises(TypeError):
        restore_names()
