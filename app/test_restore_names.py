import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.mark.parametrize(
    "users, expected_users",
    [
        (
            [{"first_name": None, "full_name": "John Doe"}],
            [{"first_name": "John", "full_name": "John Doe"}],
        ),
        (
            [{"full_name": "Jane Smith"}],
            [{"first_name": "Jane", "full_name": "Jane Smith"}],
        ),
        (
            [{"first_name": "Alice", "full_name": "Alice Wonderland"}],
            [{"first_name": "Alice", "full_name": "Alice Wonderland"}],
        ),
    ],
)
def test_restore_names(
        users: List[Dict[str, str | None]],
        expected_users: List[Dict[str, str]],
) -> None:
    restore_names(users)
    assert users == expected_users
