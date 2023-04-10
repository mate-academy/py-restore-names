import pytest
from app.restore_names import restore_names


def test_restore_names():
    # Test case with one user missing first name
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"

    # Test case with one user missing full name
    users = [
        {
            "first_name": "Sarah",
            "last_name": "Jones",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Sarah"

    # Test case with one user with a first name
    users = [
        {
            "first_name": "Tom",
            "last_name": "Johnson",
            "full_name": "Tom Johnson",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"

    # Test case with multiple users
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Mary",
            "last_name": "Smith",
            "full_name": "Mary Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Mary"

    # Test case with all users already having first name
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
