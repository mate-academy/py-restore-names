from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    users = [
        {"full_name": "John Smith", "first_name": None},
        {"full_name": "Alice Wonderland"},
        {"full_name": "Bob", "first_name": "Bob"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Alice"
    assert users[2]["first_name"] == "Bob"
