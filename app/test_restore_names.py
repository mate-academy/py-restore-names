import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,restore_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Bab",
                    "full_name": "Mariana Bab"
                },
                {
                    "last_name": "Bab",
                    "full_name": "Mariana Bab"
                }
            ],
            [
                {
                    "first_name": "Mariana",
                    "last_name": "Bab",
                    "full_name": "Mariana Bab"
                },
                {
                    "first_name": "Mariana",
                    "last_name": "Bab",
                    "full_name": "Mariana Bab"
                }
            ]
        )
    ]
)
def test_restore_names_correctly(
        users: list[dict],
        restore_users: list[dict]
) -> None:
    restore_names(users)
    assert users == restore_users
