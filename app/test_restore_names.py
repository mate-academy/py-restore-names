from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Anna"


def test_restore_names_when_first_name_missing() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"last_name": "Brown", "full_name": "Alice Brown"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
    assert users[1]["first_name"] == "Alice"


def test_restore_names_does_not_return_anything() -> None:
    users = [{"first_name": None, "last_name": "Doe", "full_name": "John Doe"}]
    result = restore_names(users)
    assert result is None
