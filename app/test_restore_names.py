import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "initial_users, complite_users",
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
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        )
    ]
)
def test_restore_names(
        initial_users: List[dict],
        complite_users: List[dict]
) -> None:
    restore_names(initial_users)
    assert initial_users == complite_users
