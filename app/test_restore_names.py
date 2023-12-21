import pytest
from app.restore_names import restore_names


def test_restore_names():
    # Test case with missing or None first_name
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
    ]
    restore_names(users)
    assert users == [
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
    ]

    # Test case with already existing first_name
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "full_name": "Bob Johnson",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "full_name": "Bob Johnson",
        },
    ]

if __name__ == "__main__":
    pytest.main()
