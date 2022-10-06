import pytest
from typing import List

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,restore_users",
    [
        pytest.param(
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
            ],
            id="test checks when first_name is None"
        ),
        pytest.param(
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
            ],
            id="test checks when first_name is missing"
        )
    ]
)
def test_checks_first_name(
        users: List[dict], restore_users: List[dict]
) -> None:
    restore_names(users)
    assert users == restore_users
