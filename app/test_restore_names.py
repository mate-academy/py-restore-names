import copy

import pytest

from app import restore_names as main


@pytest.fixture
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
    ]


def test_should_restore_first_name_when_it_is_none(users: list) -> None:
    main.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_key_is_missing(users: list) -> None:
    main.restore_names(users)
    assert users[1]["first_name"] == "Mike"


def test_should_not_return_anything(users: list) -> None:
    assert main.restore_names(users) is None


def test_should_modify_users_in_place(users: list) -> None:
    main.restore_names(users)
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
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    expected = copy.deepcopy(users)
    main.restore_names(users)
    assert users == expected


def test_should_not_change_other_fields(users: list) -> None:
    main.restore_names(users)
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"
    assert users[1]["last_name"] == "Adams"
    assert users[1]["full_name"] == "Mike Adams"


def test_should_work_with_empty_list() -> None:
    users = []
    main.restore_names(users)
    assert users == []


def test_should_restore_names_for_many_users() -> None:
    users = [
        {"first_name": None, "last_name": "A", "full_name": "Ann A"},
        {"last_name": "B", "full_name": "Bob B"},
        {"first_name": "Cat", "last_name": "C", "full_name": "Cat C"},
    ]
    main.restore_names(users)
    assert [user["first_name"] for user in users] == ["Ann", "Bob", "Cat"]
