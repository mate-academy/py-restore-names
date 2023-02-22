import pytest
from app.restore_names import restore_names


def test_restore_names():
    # Test case 1: all users have first_name
    users = [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"first_name": "Bob", "last_name": "Johnson", "full_name": "Bob Johnson"},
        {"first_name": "Charlie", "last_name": "Brown", "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"first_name": "Bob", "last_name": "Johnson", "full_name": "Bob Johnson"},
        {"first_name": "Charlie", "last_name": "Brown", "full_name": "Charlie Brown"},
    ]

    # Test case 2: some users don't have first_name
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "", "last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "", "last_name": "Doe", "full_name": "Jane Doe"},
    ]

    # Test case 3: all users don't have first_name
    users = [
        {"last_name": "Smith", "full_name": "Alice Smith"},
        {"last_name": "Johnson", "full_name": "Bob Johnson"},
        {"last_name": "Brown", "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"first_name": "Bob", "last_name": "Johnson", "full_name": "Bob Johnson"},
        {"first_name": "Charlie", "last_name": "Brown", "full_name": "Charlie Brown"},
    ]

    # Test case 4: one user has first_name and another doesn't have first_name
    users = [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]

    # Test case 5: only users with missing first names
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]



