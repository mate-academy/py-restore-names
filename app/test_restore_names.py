import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        # Case 1: first_name is None or missing
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
        # Case 2: all first_names already present
        (
            [
                {"first_name": "Alice",
                 "last_name": "Brown",
                 "full_name": "Alice Brown"},
                {"first_name": "Bob",
                 "last_name": "Smith",
                 "full_name": "Bob Smith"},
            ],
            [
                {"first_name": "Alice",
                 "last_name": "Brown",
                 "full_name": "Alice Brown"},
                {"first_name": "Bob",
                 "last_name": "Smith",
                 "full_name": "Bob Smith"},
            ],
        ),
        # Case 3: mixed None, missing, and present
        (
            [
                {"first_name": None,
                 "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": "Jane",
                 "last_name": "Doe",
                 "full_name": "Jane Doe"},
                {"last_name": "Black",
                 "full_name": "Jack Black"},
            ],
            [
                {"first_name": "John",
                 "last_name": "Doe",
                 "full_name": "John Doe"},
                {"first_name": "Jane",
                 "last_name": "Doe",
                 "full_name": "Jane Doe"},
                {"first_name": "Jack",
                 "last_name": "Black",
                 "full_name": "Jack Black"},
            ],
        ),
        # Case 4: empty list
        ([], []),
    ]
)
def test_restore_names(input_users: list,
                       expected_users: list
                       ) -> None:
    restore_names(input_users)
    assert input_users == expected_users
