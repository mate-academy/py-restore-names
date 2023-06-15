from typing import List

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def absent_first_name() -> list:
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


def test_no_first_name(absent_first_name: List[dict]) -> None:
    restore_names(absent_first_name)
    assert absent_first_name == [
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
