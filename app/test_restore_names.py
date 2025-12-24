from app.restore_names import restore_names


def test_should_restore_first_name_from_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_should_not_change_first_name_when_present() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"


def test_should_handle_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
