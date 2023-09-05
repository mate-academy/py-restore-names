from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_output",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe",
            }],
            [{
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            }],
            id="Test restore 'name' when first_name is None"
        ),
        pytest.param(
            [{
                "last_name": "Smith",
                "full_name": "Alice Smith",
            }],
            [{
                "first_name": "Alice",
                "last_name": "Smith",
                "full_name": "Alice Smith",
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
