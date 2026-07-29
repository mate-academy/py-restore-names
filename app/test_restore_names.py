import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_before, users_after",
    [
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
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Nike Adams",
                }
            ],
            [
                {
                    "first_name": "Nike",
                    "last_name": "Adams",
                    "full_name": "Nike Adams",
                }
            ]
        )
    ]
)
def test_missing_first_name_field(
        users_before: list,
        users_after: list
) -> None:
    restore_names(users_before)
    assert users_after == users_before
