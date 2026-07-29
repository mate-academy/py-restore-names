from app.restore_names import restore_names


def test_if_first_name_not_in_user() -> None:
    users = [{"full_name": "John Smith"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_first_name_when_none() -> None:
    users = [{"full_name": "Alice Cooper", "first_name": None}]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_first_name_in_user() -> None:
    users = [{"full_name": "Kyle Smith", "first_name": "Kyle"}]
    restore_names(users)
    assert users[0]["first_name"] == "Kyle"
