import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_users, expected_users",
    [
        (
            [{
                "first_name": None,
                "last_name": "Black",
                "full_name": "John Black",
            }],
            [{
                "first_name": "John",
                "last_name": "Black",
                "full_name": "John Black",
            }],
        ),
        (
            [{
                "last_name": "Adams",
                "full_name": "Alice Adams",
            }],
            [{
                "first_name": "Alice",
                "last_name": "Adams",
                "full_name": "Alice Adams",
            }],
        ),
        (
            [{
                "first_name": "Jack",
                "last_name": "Black",
                "full_name": "Jack Black",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Black",
                "full_name": "Jack Black",
            }],
        ),
    ],
)
def test_restore_names_parametric(
        initial_users: List[dict],
        expected_users: List[dict]
) -> None:
    restore_names(initial_users)
    assert initial_users == expected_users
