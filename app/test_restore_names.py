from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_output",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holly",
                "full_name": "Jack Holly",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holly",
                "full_name": "Jack Holly",
            }],
            id="Test restore 'name' when first_name is None"
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
            id="Restore first_name when is no"
        )
    ]
)
def test_restore_names(
        user: List[dict],
        expected_output: List[dict],
) -> None:
    user_restore = [user]
    restore_names(user)
    assert user_restore == [expected_output]
