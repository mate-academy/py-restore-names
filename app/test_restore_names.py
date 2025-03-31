from app.restore_names import restore_names

# write your tests here


def test_restore_names() -> None:
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
        assert user[0].get("first_name") == "Jack"
        assert user[1].get("first_name") == "Mike"
