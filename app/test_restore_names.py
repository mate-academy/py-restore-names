import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users, test_description",
    [
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
            "Restore names with None first_name",
        ),
        (
            [
                {"last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "John",
                 "last_name": "Doe",
                 "full_name": "John Doe"},
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "John",
                 "last_name": "Doe",
                 "full_name": "John Doe"},
            ],
            "Restore names with missing first_name",
        ),
        (
            [
                {
                    "first_name": "Alice",
                    "last_name": "Smith",
                    "full_name": "Alice Smith",
                },
                {"first_name": "Bob",
                 "last_name": "Jones",
                 "full_name": "Bob Jones"},
            ],
            [
                {
                    "first_name": "Alice",
                    "last_name": "Smith",
                    "full_name": "Alice Smith",
                },
                {"first_name": "Bob",
                 "last_name": "Jones",
                 "full_name": "Bob Jones"},
            ],
            "Restore names with existing first_name",
        ),
    ],
    ids=["test_none_first_name",
         "test_missing_first_name",
         "test_existing_first_name"],
)
def test_restore_names(
        input_users: list[dict],
        expected_users: list[dict],
        test_description: str
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
