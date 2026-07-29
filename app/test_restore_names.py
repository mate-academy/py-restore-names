from app.restore_names import restore_names


def test_restore_names_if_no_first_name() -> None:
    user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Mike"


def test_restore_names_if_first_name_none() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_restore_names_if_ok() -> None:
    user = [
        {
            "first_name": "John",
            "last_name": "Qwerty",
            "full_name": "John Qwerty",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "John"
