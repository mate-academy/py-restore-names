from app.restore_names import restore_names


def test_restore_names_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_empty() -> None:
    users = [{"full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_be() -> None:
    users = [{"first_name": "Jack", "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
