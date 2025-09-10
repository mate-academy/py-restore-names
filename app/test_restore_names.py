from app.restore_names import restore_names


def test_restore_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_missing_first_name() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_multiple_users_mixed_cases() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown",
        },
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown",
        },
    ]
