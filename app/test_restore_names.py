from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith"
        },
        {
            "last_name": "Doe",
            "full_name": "Jane Doe"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
