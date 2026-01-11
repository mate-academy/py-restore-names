from typing import Callable, Any
import copy
import pytest
from app.restore_names import restore_names


@pytest.fixture
def make_users() -> Callable:
    def _make(template: object) -> Any:
        return copy.deepcopy(template)
    return _make


def test_returns_none_and_mutates_in_place(make_users: Callable) -> None:
    users = make_users([
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ])
    result = restore_names(users)
    assert result is None
    assert users[0]["first_name"] == "Jack"


def test_sets_first_name_when_key_missing(make_users: Callable) -> None:
    users = make_users([
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ])
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_does_not_touch_existing_first_name(make_users: Callable) -> None:
    users = make_users([
        {
            "first_name": "Emma",
            "last_name": "Stone",
            "full_name": "Emma Stone"
        },
    ])
    restore_names(users)
    assert users[0]["first_name"] == "Emma"


@pytest.mark.parametrize("full_name, expected", [
    ("  Mike  Adams  ", "Mike"),
    ("Mike    Adams", "Mike"),
    ("Mary Jane Watson", "Mary"),
])
def test_whitespace_and_multiword_full_name(
        make_users: Callable,
        full_name: str,
        expected: str
) -> None:
    users = make_users([
        {"first_name": None, "last_name": "X", "full_name": full_name},
    ])
    restore_names(users)
    assert users[0]["first_name"] == expected
