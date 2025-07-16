from app.restore_names import restore_names


def test_restore_none_first_name() -> None:
    users = [{"first_name": None, "last_name": "Doe", "full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_missing_first_name_key() -> None:
    users = [{"last_name": "Smith", "full_name": "Alice Smith"}]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_skip_existing_first_name() -> None:
    users = [
        {"first_name": "Emily",
         "last_name": "Clark",
         "full_name": "Emily Clark"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"  # Should stay unchanged


def test_multiple_users_mixed_cases() -> None:
    users = [
        {"first_name": None, "last_name": "Lee", "full_name": "Bruce Lee"},
        {"last_name": "Bond",
         "full_name": "James Bond"},
        {"first_name": "Ada",
         "last_name": "Lovelace",
         "full_name": "Ada Lovelace"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bruce"
    assert users[1]["first_name"] == "James"
    assert users[2]["first_name"] == "Ada"


def test_full_name_with_multiple_parts() -> None:
    users = [{"last_name": "Kumar", "full_name": "Rajeev Singh Kumar"}]
    restore_names(users)
    assert users[0]["first_name"] == "Rajeev"
