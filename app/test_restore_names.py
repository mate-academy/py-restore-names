from app.restore_names import restore_names


def test_restore_only_none_names() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_only_missing_names() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
