import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "list_with_full_name,expected_result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            id="then first name equals None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },

            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },

            ],
            id="then first name not in the dictionary"
        ),
        pytest.param(
            [
                {
                    "last_name": "Smith",
                    "full_name": "Mike Smith"
                },
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "John Black"
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Smith",
                    "full_name": "Mike Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Black",
                    "full_name": "John Black"
                }
            ],
            id="checking two dictionaries"
        )
    ]
)
def test_total_function(
    list_with_full_name: List[dict],
    expected_result: List[dict]
) -> None:
    restore_names(list_with_full_name)
    assert list_with_full_name == expected_result
