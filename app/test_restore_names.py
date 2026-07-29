from app.restore_names import restore_names


def test_restore_names_if_first_name_is_none() -> None:
    test_user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(test_user)
    assert test_user[0]["first_name"] == "Jack"


def test_restore_names_if_first_name_not_exist() -> None:
    test_user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(test_user)
    assert test_user[0]["first_name"] == "Mike"
