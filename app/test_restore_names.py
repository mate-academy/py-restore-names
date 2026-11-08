import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users() -> list:
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
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]


def test_should_restore_first_name_when_it_is_none(users: list) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_it_is_missing(users: list) -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"


def test_should_not_change_existing_first_name(users: list) -> None:
    restore_names(users)
    assert users[2]["first_name"] == "Anna"


def test_should_return_none(users: list) -> None:
    assert restore_names(users) is None


def test_should_restore_names_as_in_example() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
