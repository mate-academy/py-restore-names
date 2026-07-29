from app.restore_names import restore_names


def test_restore_names_with_none() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_missing_key() -> None:
    users = [
        {"full_name": "Mike Adams"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_correct_first_name() -> None:
    users = [
        {"first_name": "George", "full_name": "George White"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "George"


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
