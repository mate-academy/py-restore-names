import pytest

from app import restore_names


@pytest.fixture
def users() -> list:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"},]


def test_first_no_data(users: list) -> None:
    del users[0]["first_name"]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_first_name_is_none(users: list) -> None:
    users[0]["first_name"] = None
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"
