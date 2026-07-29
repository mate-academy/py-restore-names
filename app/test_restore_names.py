from app.restore_names import restore_names


users = [
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


def test_add_first_name_if_none() -> None:
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_add_first_name_if_not_in_dict() -> None:
    restore_names(users)
    assert users[1]["first_name"] == "Mike"
