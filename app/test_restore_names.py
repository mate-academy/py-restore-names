from app.restore_names import restore_names


def test_restore_first_name_from_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_when_missing_key() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_does_not_override_existing_first_name() -> None:
    users = [
        {"first_name": "Sarah", "last_name": "Connor",
         "full_name": "Sarah Connor"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Sarah"
