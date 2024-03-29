import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_users, restored_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "John Black",
                },
                {
                    "last_name": "Smith",
                    "full_name": "Jake Smith"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Black",
                    "full_name": "John Black",
                },
                {
                    "first_name": "Jake",
                    "last_name": "Smith",
                    "full_name": "Jake Smith"
                }
            ]
        )
    ]
)
def test_restore_names(
        initial_users: list[dict],
        restored_users: list[dict]
) -> None:
    restore_names(initial_users)
    assert initial_users == restored_users
