import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_from_database() -> dict:
    return {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }


def test_restore_names_without_first_name_key(user_from_database) -> None:
    del user_from_database["first_name"]
    restore_names([user_from_database])
    assert user_from_database["first_name"] == "Mike"


def test_restore_names_when_first_name_key_is_none(user_from_database) -> None:
    user_from_database["first_name"] = None
    restore_names([user_from_database])
    assert user_from_database["first_name"] == "Mike"


def test_restore_names_when_first_name_key_is_correct(user_from_database) -> None:
    restore_names([user_from_database])
    assert user_from_database["first_name"] == "Mike"
