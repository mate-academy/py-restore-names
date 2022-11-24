# import pytest
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Kenobi",
            "full_name": "Ben Kenobi"
        },
        {
            "last_name": "Skywalker",
            "full_name": "Luke Skywalker"
        }
    ]
    restored_users = [
        {
            "first_name": "Ben",
            "last_name": "Kenobi",
            "full_name": "Ben Kenobi"
        },
        {
            "first_name": "Luke",
            "last_name": "Skywalker",
            "full_name": "Luke Skywalker"
        }
    ]
    restore_names(users)
    assert users == restored_users
