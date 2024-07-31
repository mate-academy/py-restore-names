import copy

import pytest

from app.restore_names import restore_names


@pytest.fixture
def user_template() -> list:
    return [
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


def test_function_restores_first_name_from_none(user_template: list) -> None:
    initial_users = copy.deepcopy(user_template)
    for user in user_template:
        user["first_name"] = None
    restore_names(user_template)
    assert user_template == initial_users


def test_function_restores_first_name_from_deleted(
        user_template: list
) -> None:
    initial_users = copy.deepcopy(user_template)
    for user in user_template:
        del user["first_name"]
    restore_names(user_template)
    assert user_template == initial_users


def test_function_does_nothing_if_first_name_is_valid(
        user_template: list
) -> None:
    initial_users = copy.deepcopy(user_template)
    restore_names(user_template)
    assert user_template == initial_users
