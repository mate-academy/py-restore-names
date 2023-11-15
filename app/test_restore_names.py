import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
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
        ],
    ),
    (
        [
            {"first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe"},
            {"first_name": "Alice",
             "last_name": "Smith",
             "full_name": "Alice Smith"},
        ],
        [
            {"first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe"},
            {"first_name": "Alice",
             "last_name": "Smith",
             "full_name": "Alice Smith"},
        ],
    ),
    (
        [],
        [],
    ),
])
def test_restore_names(input_users: list, expected_users: list) -> None:
    restore_names(input_users)
    assert input_users == expected_users
