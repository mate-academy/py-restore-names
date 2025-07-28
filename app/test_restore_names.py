from app.restore_names import restore_names


def test_restore_missing_first_name():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Smith"},
        {"last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"


def test_restore_does_not_change_existing_first_name():
    users = [
        {"first_name": "Emily", "last_name": "Blunt", "full_name": "Emily Blunt"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Emily"


def test_restore_handles_multiple_users():
    users = [
        {"first_name": None, "last_name": "Brown", "full_name": "Charlie Brown"},
        {"first_name": "Snoopy", "last_name": "Dog", "full_name": "Snoopy Dog"},
        {"last_name": "Griffin", "full_name": "Peter Griffin"},
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Charlie"
    assert users[1]["first_name"] == "Snoopy"
    assert users[2]["first_name"] == "Peter"

