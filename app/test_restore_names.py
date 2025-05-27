from typing import Callable
import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_info() -> dict:
    return user(
        last_name="Holy",
        full_name="Jack Holy",
    )


def test_restore_names_without_name(user_info: Callable) -> None:
    assert restore_names(user_info) == "first_name: ""Jack"


def test_restore_names_when_name_is_none(user_info: Callable) -> None:
    user.first_name = None
    assert restore_names(user_info) == "first_name: ""Jack"
