# tests/test_restore_names.py
import pytest
from app.restore_names import restore_names
from typing import List, Dict


def test_restore_names_empty_list() -> None:
    users: List[Dict] = []
    restore_names(users)
    assert users == []


def test_restore_names_with_none_first_name() -> None:
    users: List[Dict] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_with_missing_first_name() -> None:
    users: List[Dict] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names_with_existing_first_name() -> None:
    users: List[Dict] = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]


def test_restore_names_mixed_users() -> None:
    users: List[Dict] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Jane Smith",
        }
    ]
    restore_names(users)
    assert users == [
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
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        }
    ]


@pytest.mark.parametrize(
    "initial_users, expected_users",
    [
        (
            [],
            [],
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
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ],
        ),
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
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Jane Smith",
                }
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
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "full_name": "Jane Smith",
                }
            ],
        ),
    ],
)
def test_restore_names_parametrized(
    initial_users: List[Dict], expected_users: List[Dict]
) -> None:
    restore_names(initial_users)
    assert initial_users == expected_users
