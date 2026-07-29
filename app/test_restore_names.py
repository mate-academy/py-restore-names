import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, user_with_first",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "last_name": "Morrison",
                    "full_name": "Carl Morrison"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": "Carl",
                    "last_name": "Morrison",
                    "full_name": "Carl Morrison"
                }
            ]
        )
    ]
)
def test_should_restore_first_name(users: list, user_with_first: list) -> None:
    restore_names(users)
    assert users == user_with_first
