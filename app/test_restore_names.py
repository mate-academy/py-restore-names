import pytest
from app.restore_names import restore_names


def test_restores_all_names():
    users = [
        {
            "full_name": "John Smith",
        },
        {
            "first_name": None,
            "full_name": "Kate Black",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "full_name": "John Smith",
        },
        {
            "first_name": "Kate",
            "full_name": "Kate Black",
        },
    ]
