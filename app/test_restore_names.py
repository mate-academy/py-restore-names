from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [{"full_name": "Bob Jonson"}]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_restore_first_name_with_none() -> None:
    users = [{"first_name": None, "full_name": "Bob Jonson"}]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_save_first_name_when_existing_first_name() -> None:
    users = [{"first_name": "Bob", "full_name": "Bob Jonson"}]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"
