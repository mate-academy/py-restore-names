import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_dict, expected",
    [
        (
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ),
        (
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        )
    ],
    ids=[
        "First name set to None",
        "First none doesn't exist"
    ]
)
def test_restore_names(user_dict: List[dict], expected: List[dict]) -> None:
    assert restore_names(user_dict) == expected
