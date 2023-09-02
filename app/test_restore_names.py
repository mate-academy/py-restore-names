from typing import List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_result",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            id="Test restore when 'name' is None"
        ),
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            id="Test restore when no 'name'"
        )
    ]
)
def test_restore_names(user: List[dict], expected_result: List[dict]) -> None:
    user_to_restore = user

    restore_names(user)

    assert user_to_restore == expected_result
