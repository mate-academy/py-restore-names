import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "full_name": "Jane Smith"
                },
                {
                    "last_name": "Brown",
                    "full_name": "Charlie Brown"
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe"
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "full_name": "Jane Smith"
                },
                {
                    "first_name": "Charlie",
                    "last_name": "Brown",
                    "full_name": "Charlie Brown"
                },
            ],
        ),
    ],
)
def test_restore_names(
    input_users: list[dict],
    expected_users: list[dict]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
