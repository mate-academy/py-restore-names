from typing import List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
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
                }
            ],
            id="should restore missing first name"
        ),
        pytest.param(
            [
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor"
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                }
            ],
            [
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor"
                },
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                }
            ],
            id="first name already exists"
        ),
        pytest.param(
            [
                {
                    "last_name": "Smith",
                    "full_name": "Anna Smith"
                },
                {
                    "last_name": "Brown",
                    "full_name": "Lisa Brown"
                }
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
                }
            ],
            id="should restore if no 'first name' key"
        ),
    ]
)
def test_restore_names(
        users: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(users)
    assert users == expected_users
