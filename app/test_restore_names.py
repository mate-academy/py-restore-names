from app.restore_names import restore_names


def test_restore_names_with_none_and_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]

    expected_users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]

    restore_names(users)
    assert users == expected_users


def test_restore_names_with_no_changes_needed() -> None:
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]

    expected_users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]

    restore_names(users)
    assert users == expected_users


def test_restore_names_with_empty_list() -> None:
    users = []
    expected_users = []

    restore_names(users)
    assert users == expected_users
