from app.restore_names import restore_names


def test_restore_names_with_none():
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_missing_key():
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_existing_first_name():
    users = [{"first_name": "John", "full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_empty_list():
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_users():
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
