from typing import List
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected", [
    ([
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ],
        [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]),
    ([
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Bob", "last_name": "Smith", "full_name": "Bob Smith"}
    ],
        [
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "Bob", "last_name": "Smith", "full_name": "Bob Smith"}
    ]),
    ([
        {"first_name": "Alice", "last_name": "Johnson",
         "full_name": "Alice Johnson"},
        {"first_name": "Bob", "last_name": "Smith", "full_name": "Bob Smith"}
    ],
        [
        {"first_name": "Alice", "last_name": "Johnson",
         "full_name": "Alice Johnson"},
        {"first_name": "Bob", "last_name": "Smith", "full_name": "Bob Smith"}
    ])
])
def test_restore_names(users: List[dict], expected: List[dict]) -> None:
    restore_names(users)
    assert users == expected
