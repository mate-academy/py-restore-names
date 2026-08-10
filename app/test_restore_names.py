from app.restore_names import restore_names


def test_restore_none_or_missing() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_existing() -> None:
    users = [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "John"
