from typing import List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_output",
    [
        pytest.param(
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
                },
            ],
            id="normal-case",
        ),
        pytest.param(
            [
                {
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                },
            ],
            [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "full_name": "Jane Doe",
                },
            ],
            id="single-user",
        ),
        pytest.param(
            [],
            [],
            id="empty-list",
        ),
    ],
)
def test_restore_names(users: List[dict], expected_output: List[dict]):
    restore_names(users)
    assert users == expected_output
