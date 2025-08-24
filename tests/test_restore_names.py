from app.restore_names import restore_names

def test_restore_names_basic():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Bell", "full_name": "Anna Bell"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"

def test_full_name_with_middle_name():
    users = [
        {"first_name": None, "last_name": "Stone", "full_name": "Liam Oliver Stone"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Liam"

def test_missing_full_name():
    users = [
        {"first_name": None, "last_name": "NoName"}
    ]
    restore_names(users)
    assert users[0].get("first_name") is None
