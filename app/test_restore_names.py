from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_absent_name() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_existing_name() -> None:
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
