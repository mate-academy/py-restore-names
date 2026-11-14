import pytest

from app import restore_names


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
    ]


def test_should_restore_first_name_when_it_is_none(users: list[dict]) -> None:
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_key_is_missing(
    users: list[dict],
) -> None:
    restore_names.restore_names(users)
    assert users[1]["first_name"] == "Mike"


def test_should_restore_all_users(users: list[dict]) -> None:
    restore_names.restore_names(users)
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
    ]


def test_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Johnny",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Johnny"


def test_should_not_return_anything(users: list[dict]) -> None:
    assert restore_names.restore_names(users) is None


def test_should_work_with_empty_list() -> None:
    users = []
    restore_names.restore_names(users)
    assert users == []
