import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}
             ],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}
             ],
        ),
        (
            [{"last_name": "Adams",
              "full_name": "Mike Adams"}
             ],
            [{"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}],
        ),
        (
            [{"first_name": "Alice",
              "last_name": "Smith",
              "full_name": "Alice Smith"}
             ],
            [{"first_name": "Alice",
              "last_name": "Smith",
              "full_name": "Alice Smith"}
             ],
        ),
        (
            [],
            [],
        ),
    ]
)
def test_restore_names(
        input_data: List[dict],
        expected_output: List[dict]
) -> None:
    restore_names(input_data)
    assert input_data == expected_output
