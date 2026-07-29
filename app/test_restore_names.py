import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Alice",
                    "last_name": "Jones",
                    "full_name": "Alice Jones"
                }
            ],
            [
                {
                    "first_name": "Alice",
                    "last_name": "Jones",
                    "full_name": "Alice Jones"
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": "Bob",
                    "last_name": "Jones",
                    "full_name": "Bob Jones"
                },
                {
                    "last_name": "Brown",
                    "full_name": "Mary Brown"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": "Bob",
                    "last_name": "Jones",
                    "full_name": "Bob Jones"
                },
                {
                    "first_name": "Mary",
                    "last_name": "Brown",
                    "full_name": "Mary Brown"
                }
            ]
        )
    ]
)
def test_correct_names(users: list[dict], expected: dict) -> None:
    restore_names(users)
    assert users == expected
