from app.restore_names import restore_names


def test_restore_names_with_none_jack() -> str:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_not_jack() -> str:
    users = [{"full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_name_none_mike() -> str:
    users = [{"first_name": None, "full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_name_not_mike() -> str:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_with_none_or_not() -> str:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
