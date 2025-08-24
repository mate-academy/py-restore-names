from app.restore_names import restore_names

def test_restore_names_basic():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Smith"},
        {"last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"

def test_restore_names_no_full_name():
    users = [
        {"first_name": None, "last_name": "Unknown"},
        {"last_name": "Anonymous"},
    ]
    restore_names(users)
    # first_name не должен быть установлен, так как full_name отсутствует
    assert users[0].get("first_name") is None
    assert "first_name" not in users[1]

def test_restore_names_already_set():
    users = [
        {"first_name": "Alice", "last_name": "Wonderland", "full_name": "Alice Wonderland"},
        {"first_name": "Bob", "last_name": "Builder", "full_name": "Bob Builder"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
