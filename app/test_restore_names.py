from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [{"first_name": None, "full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_with_none_key() -> None:
    users = [{"full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_with_key_unchangeable() -> None:
    users = [{"first_name": "Mr", "full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mr"
