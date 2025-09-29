from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": "Jane Smith", "first_name": "Jane"},
        {"full_name": "Alice Johnson"},
        {"full_name": "Bob Brown", "first_name": None},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"  # Should remain unchanged
    assert users[2]["first_name"] == "Alice"
    assert users[3]["first_name"] == "Bob"
