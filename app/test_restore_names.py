import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
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
            ],
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
            ],
        ),
        (
            [
                {
                    "first_name": "Jack",
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
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": None,
                    "full_name": "John Doe",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": None,
                    "full_name": "John Doe",
                }
            ],
        ),
    ],
)
def test_restore_names(users: List, expected: List) -> None:
    restore_names(users)
    assert users == expected
