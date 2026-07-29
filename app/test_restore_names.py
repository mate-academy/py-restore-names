from typing import Any

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_users",
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
            id="boundary tests"
        )
    ]
)
def test_works_correctly(
        users: list[dict],
        expected_users: list[dict]) -> None:
    restore_names(users)
    assert users == expected_users


@pytest.mark.parametrize(
    "element, expected_error",
    [
        (1234, TypeError)
    ]
)
def test_raises_errors_correctly(
        element: Any,
        expected_error: Any) -> None:
    with pytest.raises(expected_error):
        restore_names(element)
