from app.restore_names import restore_names


def test_check_name_users() -> None:
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

    assert users == [{"first_name": "Jack",
                      "last_name": "Holy", "full_name": "Jack Holy"},
                     {"last_name": "Adams", "full_name":
                         "Mike Adams", "first_name": "Mike"}]
