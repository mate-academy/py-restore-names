import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, restored_users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Lytvyn",
                    "full_name": "Oleksandr Lytvyn",
                },
                {
                    "last_name": "Bashirian",
                    "full_name": "Eliza Bashirian",
                },
            ],
            [
                {
                    "first_name": "Oleksandr",
                    "last_name": "Lytvyn",
                    "full_name": "Oleksandr Lytvyn",
                },
                {
                    "first_name": "Eliza",
                    "last_name": "Bashirian",
                    "full_name": "Eliza Bashirian",
                },
            ],
        )
    ]
)
def test_restore_names(users: list, restored_users: list) -> None:
    restore_names(users)
    assert users == restored_users
