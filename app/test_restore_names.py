from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_user, expected_user",
    [
        ([{"full_name": "Jack Holly", "first_name": None}], "Jack"),
        ([{"full_name": "Mike Adams"}], "Mike"),
        ([{"full_name": "Jack Pit", "first_name": "Jack"}], "Jack"),

    ]
)
def test_should_return_correct_result(input_user: List[dict],
                                      expected_user: str) -> None:
    restore_names(input_user)
    assert input_user[0]["first_name"] == expected_user
