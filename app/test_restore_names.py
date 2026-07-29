from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_missing_key() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_existing_name() -> None:
    users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
