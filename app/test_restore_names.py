from app.restore_names import restore_names


def test_key_first_name_absent() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_name_more_that_one_users() -> None:
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
