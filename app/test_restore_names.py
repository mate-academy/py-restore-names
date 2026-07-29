import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize(
    "users, fixed_users",
    [
        (
            [
                {"first_name": None,
                 "last_name": "Holy", "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
                {"first_name": "Anna",
                 "last_name": "Smith", "full_name": "Anna Smith"},
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy", "full_name": "Jack Holy"},
                {"first_name": "Mike",
                 "last_name": "Adams", "full_name": "Mike Adams"},
                {"first_name": "Anna",
                 "last_name": "Smith", "full_name": "Anna Smith"},
            ],
        ),
        ([], []),
        (
            [{"last_name": "Brown",
              "full_name": "Charlie Brown"}],
            [{"first_name": "Charlie",
              "last_name": "Brown", "full_name": "Charlie Brown"}],
        ),
        (
            [{"first_name": "Lily",
              "last_name": "Evans", "full_name": "Lily Evans"}],
            [{"first_name": "Lily",
              "last_name": "Evans", "full_name": "Lily Evans"}],
        ),
    ],
)
def test_restore_names(users: List[dict], fixed_users: List[dict]) -> None:
    restore_names(users)
    assert users == fixed_users
