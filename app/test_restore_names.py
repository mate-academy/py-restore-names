from typing import List, Dict, Optional
import pytest
from app.restore_names import restore_names

User = Dict[str, Optional[str]]


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
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                },
            ],
        ),
        ([], []),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Brown",
                    "full_name": "Charlie Brown Jr.",
                },
            ],
            [
                {
                    "first_name": "Charlie",
                    "last_name": "Brown",
                    "full_name": "Charlie Brown Jr.",
                },
            ],
        ),
        (
            [
                {
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Taylor",
                    "full_name": "Chris Taylor",
                },
                {
                    "first_name": "",
                    "last_name": "Jordan",
                    "full_name": "Michael Jordan",
                },
            ],
            [
                {
                    "first_name": "Chris",
                    "last_name": "Taylor",
                    "full_name": "Chris Taylor",
                },
                {
                    "first_name": "",
                    "last_name": "Jordan",
                    "full_name": "Michael Jordan",
                },
            ],
        ),
    ],
)
def test_restore_names(users: List[User], expected: List[User]) -> None:
    restore_names(users)
    assert users == expected
