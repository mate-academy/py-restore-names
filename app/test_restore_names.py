from typing import List
from restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [{"first_name": None,
              "last_name": "Skywalker",
              "full_name": "Luke Skywalker"}],
            [{"first_name": "Luke",
              "last_name": "Skywalker",
              "full_name": "Luke Skywalker"}]
        ),
        (
            [{"last_name": "White",
              "full_name": "Walter White"}],
            [{"first_name": "Walter",
              "last_name": "White",
              "full_name": "Walter White"}]
        ),
        (
            [{"first_name": "Rick",
              "last_name": "Sanchez",
              "full_name": "Rick Sanchez"}],
            [{"first_name": "Rick",
              "last_name": "Sanchez",
              "full_name": "Rick Sanchez"}]
        ),
    ]
)


def test_restore_names(input_users: List[dict], expected_users: List[dict]) -> None:
    restore_names(input_users)
    assert input_users == expected_users

