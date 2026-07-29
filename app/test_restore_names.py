from app import restore_names


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        }
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_names_handles_multiple_users_at_once() -> None:
    users = [
        {"full_name": "John Doe"},
        {"first_name": None, "full_name": "Jane Doe"}
    ]
    restore_names.restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
