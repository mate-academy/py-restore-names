from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe"
        },
        {
            "last_name": "Smith",
            "full_name": "Alice Smith"
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Bob Smith"
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe"
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith"
        },
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith"
        }
    ]
