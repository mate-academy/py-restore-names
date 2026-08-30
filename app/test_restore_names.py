import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_users_list, expected_list",
    [
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
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        ),
        (
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ]
        ),
        ([], [])
    ]
)
def test_restore_names(
        initial_users_list: List[dict],
        expected_list: List[dict]
) -> None:
    restore_names(initial_users_list)
    assert expected_list == initial_users_list
