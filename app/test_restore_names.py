import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users() -> list[dict]:
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
            "first_name": "Ann",
            "last_name": "Smith",
            "full_name": "Ann Smith",
        },
    ]


def test_should_restore_first_name_when_it_is_none(users: list[dict]) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_it_is_missing(
        users: list[dict],
) -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"


def test_should_not_change_existing_first_name(users: list[dict]) -> None:
    restore_names(users)
    assert users[2]["first_name"] == "Ann"


def test_should_restore_all_users_in_place(users: list[dict]) -> None:
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Ann",
            "last_name": "Smith",
            "full_name": "Ann Smith",
        },
    ]


def test_should_return_none(users: list[dict]) -> None:
    assert restore_names(users) is None
