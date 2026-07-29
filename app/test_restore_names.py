from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"full_name": "John Doe", "last_name": "Doe"},
        {"full_name": "Jane Smith",
         "first_name": "Jane", "last_name": "Smith"},
        {"full_name": "Bob Johnson",
         "first_name": None, "last_name": "Johnson"}
    ]
    restore_names(users)
    assert users == [
        {"full_name": "John Doe", "first_name": "John", "last_name": "Doe"},
        {"full_name": "Jane Smith",
         "first_name": "Jane", "last_name": "Smith"},
        {"full_name": "Bob Johnson",
         "first_name": "Bob", "last_name": "Johnson"}
    ]

    users = [
        {"full_name": "John Doe", "first_name": "John", "last_name": "Doe"},
        {"full_name": "Jane Smith",
         "first_name": "Jane", "last_name": "Smith"},
        {"full_name": "Bob Johnson",
         "first_name": "Bob", "last_name": "Johnson"}
    ]
    restore_names(users)
    assert users == [
        {"full_name": "John Doe", "first_name": "John", "last_name": "Doe"},
        {"full_name": "Jane Smith",
         "first_name": "Jane", "last_name": "Smith"},
        {"full_name": "Bob Johnson",
         "first_name": "Bob", "last_name": "Johnson"}
    ]

    users = [
        {"full_name": "John Doe", "last_name": "Doe"},
        {"full_name": "Jane Smith", "last_name": "Smith"},
        {"full_name": "Bob Johnson", "last_name": "Johnson"}
    ]
    restore_names(users)
    assert users == [
        {"full_name": "John Doe", "first_name": "John", "last_name": "Doe"},
        {"full_name": "Jane Smith",
         "first_name": "Jane", "last_name": "Smith"},
        {"full_name": "Bob Johnson",
         "first_name": "Bob", "last_name": "Johnson"}
    ]
