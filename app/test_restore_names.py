import pytest
from typing import List, Dict
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
                },
                {
                    "first_name": None,
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
            ],
        ),
        (
            [
                {
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
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
                {
                    "first_name": "Emily",
                    "last_name": "Jones",
                    "full_name": "Emily Jones",
                },
                {
                    "last_name": "Davis",
                    "full_name": "Mark Davis",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
                {
                    "first_name": "Emily",
                    "last_name": "Jones",
                    "full_name": "Emily Jones",
                },
                {
                    "first_name": "Mark",
                    "last_name": "Davis",
                    "full_name": "Mark Davis",
                },
            ],
        ),
        ([], []),
    ],
)
def test_restore_names(users: List[Dict], expected: List[Dict]) -> None:
    restore_names(users)
    assert users == expected
