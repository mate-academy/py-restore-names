from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"full_name": "John Doe"},
        {"first_name": None, "full_name": "Jane Smith"},
    ]
    restore_names(users)
    assert users == [
        {"full_name": "John Doe", "first_name": "John"},
        {"full_name": "Jane Smith", "first_name": "Jane"},
    ]


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {"first_name": "Alice", "full_name": "Alice Brown"},
        {"first_name": "Bob", "full_name": "Bob Green"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Alice", "full_name": "Alice Brown"},
        {"first_name": "Bob", "full_name": "Bob Green"},
    ]
