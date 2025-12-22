from app.restore_names import restore_names


def test_restore_names_fills_none_values() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_names_fills_missing_keys() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing_names() -> None:
    users = [
        {
            "first_name": "Jonathan",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jonathan"


def test_restore_names_handles_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Wonderland"},
        {"full_name": "Bob Builder"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"


def test_restore_names_returns_none() -> None:
    users = [
        {"full_name": "Test User"},
    ]

    result = restore_names(users)

    assert result is None


def test_restore_names_with_empty_list() -> None:
    users = []

    restore_names(users)

    assert users == []
