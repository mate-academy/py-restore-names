from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "first_name": "Peter",
                    "last_name": "Jones",
                    "full_name": "Peter Jones",
                }
            ],
            [
                {
                    "first_name": "Peter",
                    "last_name": "Jones",
                    "full_name": "Peter Jones",
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
        )
    ]
)
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
