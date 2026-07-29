import pytest
from typing import List, Dict
from app.restore_names import restore_names


@pytest.mark.parametrize("input_users, expected_users", [
    (
        [  # noqa: E501
            {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},  # noqa: E501
            {"last_name": "Adams", "full_name": "Mike Adams"},
        ],
        [  # noqa: E501
            {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},  # noqa: E501
            {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},  # noqa: E501
        ]
    ),
    (
        [
            {"last_name": "Smith", "full_name": "John Smith"},
            {"first_name": None, "last_name": "Doe", "full_name": "Jane Doe"},
        ],
        [  # noqa: E501
            {"first_name": "John", "last_name": "Smith", "full_name": "John Smith"},  # noqa: E501
            {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"},  # noqa: E501
        ]
    ),
    (
        [
            {"first_name": "Alice", "last_name": "Wonderland", "full_name": "Alice Wonderland"},  # noqa: E501
            {"first_name": "Bob", "last_name": "Builder", "full_name": "Bob Builder"},  # noqa: E501
        ],
        [
            {"first_name": "Alice", "last_name": "Wonderland", "full_name": "Alice Wonderland"},  # noqa: E501
            {"first_name": "Bob", "last_name": "Builder", "full_name": "Bob Builder"},  # noqa: E501
        ]
    ),
])
def test_restore_names(input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]) -> None:  # noqa: E501
    restore_names(input_users)
    assert input_users == expected_users
