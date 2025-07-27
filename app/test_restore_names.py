from app.restore_names import restore_names


def test_restore_last_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "last_name": "Smith",
            "full_name": "Alice Smith",
        }
    ]

    expected = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        }
    ]

    restore_names(users)
    assert users == expected
