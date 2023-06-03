import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def input_data() -> List:
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
def out_data() -> List:
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


def test_output_data(
        input_data: List,
        out_data: List) -> None:
    restore_names(input_data)
    assert input_data == out_data
