import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        # First test suit - None value or None key "first_name" in dict keys
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
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
                }
            ]
        ),
        # Second test suit - No changes in "first_name" dict key
        (
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
                }
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
                }
            ]
        ),
        # Third test suit - Empty lists
        (
            [],
            []
        )
    ]
)
def test_restore_names_function_if_returns_correct_result(
    users: List[dict],
    expected_users: List[dict]
) -> None:
    result = restore_names(users)
    assert result is None
    assert users == expected_users
