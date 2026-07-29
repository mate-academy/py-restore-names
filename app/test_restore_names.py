import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize("users, expected", [
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
                "first_name": None,
                "last_name": "Smith",
                "full_name": "John Smith",
            },
        ],
        [
            {
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "John Smith",
            },
        ],
    ),
    (
        [
            {
                "first_name": "Alice",
                "last_name": "Wonderland",
                "full_name": "Alice Wonderland",
            },
        ],
        [
            {
                "first_name": "Alice",
                "last_name": "Wonderland",
                "full_name": "Alice Wonderland",
            },
        ],
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "full_name": "Jane Smith",
            },
            {
                "last_name": "Black",
                "full_name": "Tom Black",
            },
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "full_name": "Jane Smith",
            },
            {
                "first_name": "Tom",
                "last_name": "Black",
                "full_name": "Tom Black",
            },
        ],
    ),
])
def test_restore_names(
        users: List[Dict[str, str]],
        expected: List[Dict[str, str]]
) -> None:
    restore_names(users)
    assert users == expected
