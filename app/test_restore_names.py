from typing import Callable

from app.restore_names import restore_names


def test_restore_names_without_name() -> None:
    user = {"last_name": "Doe", "full_name": "Jack Holy"}
    assert restore_names(user) == "first_name: ""Jack"


def test_restore_names_when_name_is_none() -> None:
    user = {"first_name": None, "last_name": "Doe", "full_name": "Jack Holy"}
    assert restore_names(user) == "first_name: ""Jack"
