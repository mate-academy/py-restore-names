from app.restore_names import restore_names


def test_restore_names_if_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]


def test_restore_names_if_firstname_missing() -> None:
    users = [
        {
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]


def test_restore_names() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
