from app.restore_names import restore_names


def test_should_restore_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_should_not_touch_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_should_handle_multiple_users_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": None,
            "last_name": "Lee",
            "full_name": "Bruce Lee",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Bruce"
