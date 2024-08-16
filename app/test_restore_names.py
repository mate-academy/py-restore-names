from typing import List

import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "value,expected_result",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}]
        ),
        (
            [{"last_name": "Adams",
             "full_name": "Mike Adams"}],
            [{"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
        ),
    ],
    ids=[
        "First name key set to None",
        "No first name key"
    ]
)
def test_cryptocurrency_action(value: List[dict],
                               expected_result: List[dict]) -> None:
    restore_names(value)
    assert value == expected_result
