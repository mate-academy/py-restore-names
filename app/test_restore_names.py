from typing import Any, Dict, List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
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
            ],
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
            ],
        ),
        (
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                }
            ],
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                }
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Alexander John Smith",
                }
            ],
            [
                {
                    "first_name": "Alexander",
                    "last_name": "Smith",
                    "full_name": "Alexander John Smith",
                }
            ],
        ),
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
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
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
                },
                {
                    "first_name": "Sarah",
                    "last_name": "Connor",
                    "full_name": "Sarah Connor",
                },
            ],
        ),
    ],
)
def test_restore_names(
    input_users: List[Dict[str, Any]],
    expected_users: List[Dict[str, Any]],
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
