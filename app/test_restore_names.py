import pytest
from typing import Dict, List

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            id="when first_name is equal to None"
        ),
        pytest.param(
            [
                {"last_name": "Adams",
                 "full_name": "Mike Adams"}
            ],
            [
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"}
            ],
            id="when first_name is missing"
        )
    ]
)
def test_restore_names(users: List[Dict], expected: List[Dict]) -> None:
    restore_names(users)
    assert users == expected
