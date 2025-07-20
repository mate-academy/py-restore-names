import pytest
import copy
from typing import Any
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    users = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy", } , {
        "last_name": "Adams",
        "full_name": "Mike Adams", } ,
    ]
    return copy.deepcopy(users)


def test_restore_names_when_none(user_template: Any) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_restore_names_when_nothing(user_template: Any) -> None:
    restore_names(user_template)
    assert user_template[1]["first_name"] == "Mike"
