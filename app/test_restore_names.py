import pytest
from app.restore_names import restore_names

from typing import List


@pytest.mark.parametrize(
    "first_value, second_value", [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
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
        )
    ]
)
def test_restore_names(
        first_value: List[dict],
        second_value: List[dict]
) -> None:
    restore_names(first_value)

    assert first_value == second_value
