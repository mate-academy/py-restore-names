from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing_first_name() -> None:
    users = [
        {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jane"


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]
