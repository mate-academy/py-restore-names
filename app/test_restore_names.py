from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_should_not_change_existing_name() -> None:
    users = [
        {
            "first_name": "Alex",
            "last_name": "Brown",
            "full_name": "John Brown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alex"


def test_restore_names_with_empty_list() -> None:
    users: list = []
    restore_names(users)
    assert users == []
