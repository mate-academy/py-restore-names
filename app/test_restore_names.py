import pytest
from app.restore_names import restore_names


def test_first_name_undefined():
    users = [
        {
            "last_name": "Rysin",
            "full_name": "Denis Rysin"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Denis"


def test_first_name_is_equal_none():
    users = [
        {
            "first_name": None,
            "last_name": "Rysin",
            "full_name": "Denis Rysin"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Denis"
