import pytest
from copy import deepcopy
from typing import List
import app.restore_names as restore_names_module


@pytest.fixture
def not_damaged_users() -> List[dict]:
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


@pytest.fixture
def damaged_users() -> List[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture
def users_with_none_first_name() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


@pytest.fixture
def users_with_missing_first_name() -> List[dict]:
    return [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_should_create_first_name_field(
    damaged_users: List[dict],
) -> None:
    restore_names_module.restore_names(damaged_users)
    for user in damaged_users:
        assert user["first_name"]


def test_first_name_equals_first_word_of_full_name(
    damaged_users: List[dict],
) -> None:
    restore_names_module.restore_names(damaged_users)
    for user in damaged_users:
        assert user["first_name"] == user["full_name"].split()[0]


def test_if_data_not_lost(
    not_damaged_users: List[dict],
) -> None:
    copy_of_data = deepcopy(not_damaged_users)
    restore_names_module.restore_names(not_damaged_users)
    assert not_damaged_users == copy_of_data


def test_restore_none_first_name(
    users_with_none_first_name: List[dict],
) -> None:
    restore_names_module.restore_names(users_with_none_first_name)
    assert users_with_none_first_name[0]["first_name"] == "Mike"


def test_restore_missing_first_name(
    users_with_missing_first_name: List[dict],
) -> None:
    restore_names_module.restore_names(users_with_missing_first_name)
    assert users_with_missing_first_name[0]["first_name"] == "Jack"
