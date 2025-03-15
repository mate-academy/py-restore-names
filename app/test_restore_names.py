import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
        ),
        (
            [
                {"last_name": "Smith",
                 "full_name": "John Smith"}
            ],
            [
                {"first_name": "John", "last_name": "Smith",
                 "full_name": "John Smith"}
            ],
        ),
        (
            [
                {"first_name": "Alice", "last_name": "Brown",
                 "full_name": "Alice Brown"}
            ],
            [
                {"first_name": "Alice", "last_name": "Brown",
                 "full_name": "Alice Brown"}
            ],
        ),
    ],
)
def test_restore_names(input_users: dict, expected_users: dict) -> None:
    restore_names(input_users)
    assert input_users == expected_users
