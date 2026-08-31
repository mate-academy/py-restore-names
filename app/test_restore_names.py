
from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_empty() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_when_first_name_already_exists() -> None:
    users = [{"first_name": "Bob", "full_name": "Robert Smith"}]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_restore_names_with_multiple_users() -> None:
    users = users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"first_name": "Anna", "full_name": "Anna Grey"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Anna"
