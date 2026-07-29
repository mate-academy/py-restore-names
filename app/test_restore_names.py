import pytest

from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> List[dict]:
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


@pytest.fixture()
def user_result() -> List[dict]:
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


def test_restore_names(
        user_template: List[dict],
        user_result: List[dict]
) -> None:
    restore_names(user_template)
    assert user_template == user_result
