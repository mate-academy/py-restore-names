import pytest
from typing import List

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {"full_name": "John Doe"},
                {"full_name": "Jane Smith", "first_name": None},
            ],
            [
                {"full_name": "John Doe", "first_name": "John"},
                {"full_name": "Jane Smith", "first_name": "Jane"},
            ],
        ),
        (
            [
                {"full_name": "John Doe", "first_name": "Johnny"},
            ],
            [
                {"full_name": "John Doe", "first_name": "Johnny"},
            ],
        ),
    ],
)
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)

    assert users == expected
