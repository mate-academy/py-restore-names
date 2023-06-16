import pytest

from typing import Callable
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_first_name_is_none(users_template: Callable) -> None:
    del users_template[0]["first_name"]
    restore_names(users_template)
    assert users_template == [{
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }]


def test_restore_names_function_who_names_none(
        users_template: Callable
) -> None:
    users_template[0]["first_name"] = None
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Mike"
