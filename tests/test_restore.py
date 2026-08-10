from app.restore_names import restore_names


def test_restore_none_or_missing() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_existing() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "John"


def test_restore_mixed() -> None:
    users = [
        {"first_name": None, "last_name": "Brown", "full_name": "Chris Brown"},
        {"first_name": "Emily", "last_name": "Clark", "full_name": "Emily Clark"},
        {"last_name": "Taylor", "full_name": "Robert Taylor"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Chris"
    assert users[1]["first_name"] == "Emily"
    assert users[2]["first_name"] == "Robert"
