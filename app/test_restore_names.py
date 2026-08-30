from app.restore_names import restore_names


def test_for_one_dict_in_list() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(user)

    assert user[0]["first_name"] == "Jack"


def test_for_dicts_in_list() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(user)
    assert user[0]["first_name"] == "Jack"
    assert user[1]["first_name"] == "Mike"
