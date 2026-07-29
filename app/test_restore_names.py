from typing import List

import pytest
from app.restore_names import restore_names


@pytest.fixture
def user_list_template_with_no_fn() -> List[dict]:
    users = [
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
    return users


@pytest.fixture
def user_list_template_with_fn() -> List[dict]:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    return users


def test_if_works_with_first_user(
        user_list_template_with_no_fn: List[dict]
) -> None:
    restore_names(user_list_template_with_no_fn)
    assert (
        user_list_template_with_no_fn[0]["first_name"] == "Jack"
    )


def test_if_works_with_second_user(
        user_list_template_with_no_fn: List[dict]
) -> None:
    restore_names(user_list_template_with_no_fn)
    assert (
        user_list_template_with_no_fn[1]["first_name"] == "Mike"
    )


def test_if_theres_a_first_name(
        user_list_template_with_fn: List[dict]
) -> None:
    restore_names(user_list_template_with_fn)
    assert (
        user_list_template_with_fn[0]["first_name"] == "Jack"
    )
