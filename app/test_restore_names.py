import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize("users, expected", [
    ([
        {"first_name": "John", "last_name": "Konor", "full_name": "John Konor"}
    ], [
        {"first_name": "John", "last_name": "Konor", "full_name": "John Konor"}
    ]),
    ([
        {"first_name": None, "last_name": "Konor", "full_name": "John Konor"}
    ], [
        {"first_name": "John", "last_name": "Konor", "full_name": "John Konor"}
    ]),
    ([
        {"last_name": "Konor", "full_name": "John Konor"}
    ], [
        {"first_name": "John", "last_name": "Konor", "full_name": "John Konor"}
    ])
])
def test_restore_name(users: List[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
