from typing import Callable

from app.restore_names import restore_names


def test_restore_names_without_name(user_info: Callable) -> None:
    user = {"last_name": "Doe", "full_name": "Jack Holy"}
    assert restore_names(user_info(user)) == "first_name: ""Jack"


def test_restore_names_when_name_is_none(user_info: Callable) -> None:
    user = {"first_name": None, "last_name": "Doe", "full_name": "Jack Holy"}
    assert restore_names(user_info(user)) == "first_name: ""Jack"
