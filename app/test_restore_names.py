import pytest
from typing import Callable
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> [dict]:
    yield [
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


def test_(users_template: Callable) -> None:
    expected_value = [
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
    restore_names(users_template)
    assert users_template == expected_value
