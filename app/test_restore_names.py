import pytest
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Adams",
            "full_name": "John Adams",

        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Sam Adams",
        },
        {
            "last_name": "Adams",
            "full_name": "Billy Adams",
        },
    ]
    expected_result = [
        {
            "first_name": "John",
            "last_name": "Adams",
            "full_name": "John Adams",

        },
        {
            "first_name": "Sam",
            "last_name": "Adams",
            "full_name": "Sam Adams",
        },
        {
            "first_name": "Billy",
            "last_name": "Adams",
            "full_name": "Billy Adams",
        },
    ]
    restore_names(users)
    assert users == expected_result
