import copy

import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]


def test_only_none_names(users_template: list) -> None:
    users_list = copy.deepcopy(users_template)
    del users_list[1]
    restore_names(users_list)
    assert users_list == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"}
    ]


def test_only_missing_names(users_template: list) -> None:
    users_list = copy.deepcopy(users_template)
    del users_list[0]
    restore_names(users_list)
    assert users_list == [
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"}
    ]
