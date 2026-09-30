from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_key_first_name() -> None:
    users = [
        {"full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_first_names_no_need() -> None:
    users = [
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)  # deve funcionar sem erro
    assert users == []
