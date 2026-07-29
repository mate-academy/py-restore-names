import pytest
from typing import List

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            ["Jack"]
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            ["Mike"]
        ),
    ]
)
def test_restore_names(
        users: List[dict],
        expected_first_names: List[str]
) -> None:
    restore_names(users)

    for i in range(len(users)):
        assert users[i]["first_name"] == expected_first_names[i]
