from app.restore_names import restore_names


def test_sets_first_name_when_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_preserves_existing_first_name() -> None:
    users = [
        {"first_name": "Alice",
         "last_name": "Blue",
         "full_name": "Alice Blue"},
        {"first_name": "Bob",
         "last_name": "Smith",
         "full_name": "Robert Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
