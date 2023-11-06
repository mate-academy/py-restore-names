from typing import List
import pytest
from app.restore_names import restore_names

# write your tests here


@pytest.mark.parametrize(
    "input_dict,output_dict",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
        )
    ]
)
def test_restore_names(input_dict: List[dict],
                       output_dict: List[dict]) -> None:
    restore_names(input_dict)
    assert input_dict == output_dict
