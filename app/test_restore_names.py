import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_with_lost_value, users_with_restored_values",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]
        )
    ]
)
def test_restore_names(users_with_lost_value: list[dict],
                       users_with_restored_values: list[dict]) -> None:
    restore_names(users_with_lost_value)
    assert users_with_lost_value == users_with_restored_values
