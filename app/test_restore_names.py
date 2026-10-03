from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_not_exist() -> None:
    users = [{"full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_already_exist() -> None:
    users = [{"first_name": "Jack", "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
