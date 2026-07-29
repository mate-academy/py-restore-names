from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_missing() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Robert Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
