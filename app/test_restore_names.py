import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Viktorovich",
                    "full_name": "Viktor Viktorovich"
                },
                {
                    "last_name": "Dmytrovich",
                    "full_name": "Dmytro Dmytrovich"
                },
                {
                    "first_name": "Nastya",
                    "last_name": "Lisovska",
                    "full_name": "Nastya Lisovska"
                }
            ],
            [
                {
                    "first_name": "Viktor",
                    "last_name": "Viktorovich",
                    "full_name": "Viktor Viktorovich"
                },
                {
                    "first_name": "Dmytro",
                    "last_name": "Dmytrovich",
                    "full_name": "Dmytro Dmytrovich"
                },
                {
                    "first_name": "Nastya",
                    "last_name": "Lisovska",
                    "full_name": "Nastya Lisovska"
                }
            ]
        )
    ]
)
def test_restore_names(users: List[dict], expected_users: List[dict]) -> None:
    restore_names(users)
    assert users == expected_users
