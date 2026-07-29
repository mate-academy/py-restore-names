import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "false_values, expected_result",
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
        )
    ]
)
def test_restore_names(false_values: List[dict],
                       expected_result: List[dict]) -> None:
    restore_names(false_values)
    assert false_values == expected_result
