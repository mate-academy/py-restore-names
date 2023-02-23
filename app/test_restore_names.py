import pytest
from typing import Callable
from app.restore_names import restore_names


@pytest.fixture()
def user_list_template() -> list:
    users = [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"last_name": "Adams",
              "full_name": "Mike Adams"},
             {"first_name": "Anna",
              "last_name": "River",
              "full_name": "Anna River"}]
    restore_names(users)
    return users


def test_change_none(user_list_template: Callable) -> None:
    assert user_list_template[0] == {"first_name": "Jack",
                                     "last_name": "Holy",
                                     "full_name": "Jack Holy"}


def test_add_field(user_list_template: Callable) -> None:
    assert user_list_template[1] == {"first_name": "Mike",
                                     "last_name": "Adams",
                                     "full_name": "Mike Adams"}


def test_not_to_change_when_ok(user_list_template: Callable) -> None:
    assert user_list_template[2] == {"first_name": "Anna",
                                     "last_name": "River",
                                     "full_name": "Anna River"}
