import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_template() -> list[dict]:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "C", "full_name": "Anna C"},
        {"first_name": None, "last_name": "D", "full_name": "Solo"}
    ]
    return [user.copy() for user in users]


def test_first_name_is_none(users_template: list[dict]) -> None:
    restore_names(users_template)
    assert users_template[0]["first_name"] == "Jack"


def test_first_name_is_empty(users_template: list[dict]) -> None:
    restore_names(users_template)
    assert users_template[1]["first_name"] == "Mike"


def test_first_name_and_last_name_are_correct(
        users_template: list[dict]
) -> None:
    restore_names(users_template)
    assert users_template[2]["first_name"] == "Anna"


def test_fullname_is_one_word(users_template: list[dict]) -> None:
    restore_names(users_template)
    assert users_template[3]["first_name"] == "Solo"
