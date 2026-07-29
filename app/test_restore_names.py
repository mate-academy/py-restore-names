from app.restore_names import restore_names


def test_restore_names_updates_missing_and_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Dams", "full_name": "Mike Dams"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]
    restore_names(users)

    assert users == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Dams", "full_name": "Mike Dams"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]
