import pytest
from app.restore_names import restore_names
from typing import Callable


@pytest.fixture()
def restored_names() -> list:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Dmytro",
            "last_name": "Bondariev",
            "full_name": "Dmytro Bondariev",
        }
    ]
    restore_names(users)
    return users


def test_missing_user_key(restored_names: Callable) -> None:
    assert restored_names[0]["first_name"] == "Jack"


def test_if_user_key_is_none(restored_names: Callable) -> None:
    assert restored_names[1]["first_name"] == "Mike"


def test_if_user_name_is_provided(restored_names: Callable) -> None:
    assert restored_names[2]["first_name"] == "Dmytro"
