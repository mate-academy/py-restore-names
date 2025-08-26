import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize("users, expected", [
    (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ],
        [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ]
    ),
    (
        [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            },
            {
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Lisa Brown"
            },
        ],
        [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            },
            {
                "first_name": "Lisa",
                "last_name": "Brown",
                "full_name": "Lisa Brown"
            },
        ]
    ),
    (
        [],
        []
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Michael Doe"
            }
        ],
        [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Michael Doe"
            }
        ]
    ),
    (
        [
            {
                "first_name": None,
                "last_name": "",
                "full_name": "Solo"
            }
        ],
        [
            {
                "first_name": "Solo",
                "last_name": "",
                "full_name": "Solo"
            }
        ]
    ),
])
def test_restore_names(
        users: List[Dict[str, str]],
        expected: List[Dict[str, str]]
) -> None:
    restore_names(users)
    assert users == expected
