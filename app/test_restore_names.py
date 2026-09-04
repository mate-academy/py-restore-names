from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_without_first_name_key() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
