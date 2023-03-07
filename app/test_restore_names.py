from typing import List

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def first_user() -> any:
    result = restore_names(
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
    )
    return result == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def second_user() -> any:
    result = restore_names(
        [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
    )
    return result == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_should_check_first_name_in_first_user(first_user: List[dict]) -> any:
    assert "first_name" == first_user


def test_should_check_first_name_in_second_user(
        second_user: List[dict]
) -> any:
    assert "first_name", second_user
