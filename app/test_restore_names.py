
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"first_name": "Bob",
         "last_name": "Johnson",
         "full_name": "Bob Johnson"},
        {"first_name": "Charlie",
         "last_name": "Brown",
         "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"first_name": "Bob",
         "last_name": "Johnson",
         "full_name": "Bob Johnson"},
        {"first_name": "Charlie",
         "last_name": "Brown",
         "full_name": "Charlie Brown"},
    ]

    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "",
         "last_name": "Doe",
         "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "",
         "last_name": "Doe",
         "full_name": "Jane Doe"},
    ]

    users = [
        {"last_name": "Smith",
         "full_name": "Alice Smith"},
        {"last_name": "Johnson",
         "full_name": "Bob Johnson"},
        {"last_name": "Brown",
         "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"first_name": "Bob",
         "last_name": "Johnson",
         "full_name": "Bob Johnson"},
        {"first_name": "Charlie",
         "last_name": "Brown",
         "full_name": "Charlie Brown"},
    ]

    users = [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]

    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": None,
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
