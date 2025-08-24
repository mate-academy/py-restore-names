from app.restore_names import restore_names


def test_restore_names_basic():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_already_set():
    users = [
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
        {"first_name": "Bob", "last_name": "Brown", "full_name": "Bob Brown"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"
    assert users[1]["first_name"] == "Bob"


def test_restore_names_missing_full_name():
    users = [
        {"first_name": None, "last_name": "Unknown"},
        {"last_name": "Anonymous"},
    ]
    restore_names(users)
    # first_name не изменится, потому что full_name нет
    assert users[0]["first_name"] is None
    assert "first_name" not in users[1]


def test_restore_names_empty_list():
    users = []
    restore_names(users)
    assert users == []
