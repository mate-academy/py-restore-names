from app.restore_names import restore_names


def test_first_name_if_its_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_first_name_if_not_exist() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)
    assert users[0]["first_name"] == "Jack"
