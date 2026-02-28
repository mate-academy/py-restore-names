# app/test_restore_names.py
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_first_name",
    [
        ({"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}, "Jack"),
        ({"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}, "Jack"),
        ({"last_name": "Adams", "full_name": "Mike Adams"}, "Mike"),
        ({"last_name": "Marley", "full_name": "Bob Marley Junior"}, "Bob"),
        ({"last_name": "Madonna", "full_name": "Madonna"}, "Madonna"),
        ({"last_name": "Test", "full_name": "   Alice   Wonderland  "}, "Alice"),
    ],
    ids=[
        "first_name_exists",
        "first_name_is_none",
        "first_name_missing",
        "multiple_words",
        "single_word",
        "extra_spaces",
    ],
)
def test_restore_names_single_user(user: dict, expected_first_name: str) -> None:
    users = [user]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"


def test_restore_names_empty_list() -> None:
    users: list[dict] = []
    restore_names(users)
    assert users == []
