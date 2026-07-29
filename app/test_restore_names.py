from app.restore_names import restore_names


def test_restore_name_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_name_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Holy",
            "fullname": "Jack Holy"
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_return_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]

    assert restore_names(users) is None
