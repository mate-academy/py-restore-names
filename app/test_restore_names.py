from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_missing() -> None:
    user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(user)
    assert user[0]["first_name"] == "Mike"
