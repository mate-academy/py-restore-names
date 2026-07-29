import pytest

from copy import deepcopy

from app.restore_names import restore_names


@pytest.fixture()
def user_list() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]


def test_restore_names_when_list_is_correct(
        user_list: list
) -> None:
    user_list_before_editing = deepcopy(user_list)

    restore_names(user_list)

    assert user_list_before_editing == user_list


def test_restore_names_when_list_is_empty(
        user_list: list
) -> None:
    user_list_before_editing = []

    empty_user_list = []

    restore_names(empty_user_list)

    assert user_list_before_editing == empty_user_list


def test_restore_names_when_first_name_is_none(
        user_list: list
) -> None:
    user_list_before_editing = deepcopy(user_list)

    user_list[0]["first_name"] = None

    restore_names(user_list)

    assert user_list == user_list_before_editing


def test_restore_names_when_there_is_not_first_name_attribute(
        user_list: list
) -> None:
    user_list_before_editing = deepcopy(user_list)

    del user_list[0]["first_name"]

    restore_names(user_list)

    assert user_list == user_list_before_editing


def test_restore_names_when_there_are_few_names(
        user_list: list
) -> None:
    user_list[0]["full_name"] = "Jack Grok Holy"

    user_list_before_editing = deepcopy(user_list)

    del user_list[0]["first_name"]

    restore_names(user_list)

    assert user_list == user_list_before_editing
