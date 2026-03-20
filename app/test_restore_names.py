from app.restore_names import restore_names


def test_restore_names_simple() -> None:
    users = [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": "Alice Smith", "first_name": "Alice"},
        {"full_name": "Bob Johnson"}
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Alice"
    assert users[2]["first_name"] == "Bob"
