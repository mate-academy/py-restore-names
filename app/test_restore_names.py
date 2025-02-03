import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ]
        ),
        (
            [
                {"last_name": "Smith",
                 "full_name": "John Smith"},
                {"last_name": "Brown",
                 "full_name": "Sarah Brown"},
            ],
            [
                {"first_name": "John",
                 "last_name": "Smith",
                 "full_name": "John Smith"},
                {"first_name": "Sarah",
                 "last_name": "Brown",
                 "full_name": "Sarah Brown"},
            ]
        ),
        (
            [
                {"first_name": "Alice",
                 "last_name": "Green",
                 "full_name": "Alice Green"},
                {"first_name": "Bob",
                 "last_name": "White",
                 "full_name": "Bob White"},
            ],
            [
                {"first_name": "Alice",
                 "last_name": "Green",
                 "full_name": "Alice Green"},
                {"first_name": "Bob",
                 "last_name": "White",
                 "full_name": "Bob White"},
            ]
        ),
        ([], []),
        (
            [
                {"first_name": None,
                 "last_name": "Shakespeare",
                 "full_name": "William Shakespeare", },
                {"last_name": "Einstein",
                 "full_name": "Albert Einstein"},
            ],
            [
                {"first_name": "William",
                 "last_name": "Shakespeare",
                 "full_name": "William Shakespeare", },
                {"first_name": "Albert",
                 "last_name": "Einstein",
                 "full_name": "Albert Einstein", },
            ]
        ),
    ]
)
def test_restore_names(
    users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(users)
    assert users == expected_users
