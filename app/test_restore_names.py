from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_key_missing() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_returns_none() -> None:
    assert restore_names([]) is None
