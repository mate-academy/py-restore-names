from app.restore_names import restore_names


def test_fill_first_name_if_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users[0].get("first_name") == "Jack"


def test_add_and_fill_first_name_if_not_exist() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)

    assert users[0].get("first_name") == "Jack"
