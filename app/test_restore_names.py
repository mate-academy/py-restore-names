from typing import Callable
import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_factory() -> Callable:
    def create_user() -> list:
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
    return create_user


def test_restore_names_sets_first_name(user_factory: Callable) -> None:
    users = user_factory()
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_mutates_in_place(user_factory: Callable) -> None:
    users = user_factory()
    original_id = id(users)
    restore_names(users)
    assert id(users) == original_id
