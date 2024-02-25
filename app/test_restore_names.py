from typing import Any, List

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_list() -> Any:
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


def test_sets_correct_name_if_it_is_none(users_list: List) -> Any:
    restore_names(users_list)

    assert users_list[0]["first_name"] == "Jack"


def test_sets_correct_name_if_it_is_absent(users_list: List) -> Any:
    restore_names(users_list)

    assert users_list[1]["first_name"] == "Mike"


def test_doesnt_return_anything(users_list: List) -> Any:
    result = restore_names(users_list)

    assert result is None
