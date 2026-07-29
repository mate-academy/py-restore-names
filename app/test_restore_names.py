import pytest
from app.restore_names import restore_names
from typing import Any


@pytest.fixture()
def users_with_missing_first_name() -> list:
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


def test_add_first_name_when_missing(
        users_with_missing_first_name: Any
) -> None:
    restore_names(users_with_missing_first_name)
    assert users_with_missing_first_name == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
