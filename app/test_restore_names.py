import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "users, users_backup",
    [
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
                    "full_name": "Jack Holy"},
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"},
            ]
        )
    ]

)
def test_restore_names(users: List, users_backup: List) -> None:
    restore_names(users)
    assert users == users_backup
