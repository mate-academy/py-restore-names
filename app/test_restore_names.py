import pytest
from app.restore_names import restore_names


def test_restore_only_none_names():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_only_missing_names():
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack"
