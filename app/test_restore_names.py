import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_in_db, expected_user",
    [
        (
            [
                {
                    "first_name": "Neo",
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"
                }
            ],
            [
                {
                    "first_name": "Neo",
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"
                }
            ],
            [
                {
                    "first_name": "Neo",
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"}
            ]
        ),
        (
            [
                {
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"}
            ],
            [
                {
                    "first_name": "Neo",
                    "last_name": "Anderson",
                    "full_name": "Neo Anderson"
                }
            ]
        )
    ]
)
def test_restore_names(user_in_db: list[dict], expected_user: dict) -> None:
    restore_names(user_in_db)

    assert user_in_db == expected_user
