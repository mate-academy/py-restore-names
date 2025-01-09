import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, restored_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
        ),
    ]
)
def test_restore_names(users: list,
                       restored_users: list) -> None:
    restore_names(users)
    assert users == restored_users, (f"Expected {restored_users}")
