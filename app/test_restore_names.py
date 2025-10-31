import pytest
from app.restore_names import restore_names


def test_restore_first_name_is_none():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_missing():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_keep_existing_first_name():
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
         }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_multiple_users():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Lara",
            "last_name": "Croft", "full_name":
            "Lara Croft"
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Lara"


def test_function_returns_none():
    users = [{"full_name": "John Doe"}]
    result = restore_names(users)
    assert result is None
