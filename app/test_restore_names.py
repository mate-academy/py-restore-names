from app.restore_names import restore_names


def test_check_if_first_name_valid() -> None:
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
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
        assert user["first_name"] is not None
