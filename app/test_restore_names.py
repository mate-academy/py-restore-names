import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def input_users_template() -> List[dict]:
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
def output_users_template() -> List[dict]:
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


def test_restore_names(input_users_template, output_users_template) -> None:
    restore_names(input_users_template)
    assert input_users_template == output_users_template
