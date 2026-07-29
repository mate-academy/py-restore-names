import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
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
        ),
        (
            [{
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            }],
            [{
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            }],
        ),
        (
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe"
                },
                {
                    "first_name": "Alice",
                    "last_name": "Smith",
                    "full_name": "Alice Smith"
                },
            ],
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe"
                },
                {
                    "first_name": "Alice",
                    "last_name": "Smith",
                    "full_name": "Alice Smith"
                },
            ],
        ),
    ],
    ids=["missing_names", "all_names_exist", "no_changes_needed"],
)
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
