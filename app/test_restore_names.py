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


def test_restore_names() -> None:
    restore_names(users)
    for user in users:
        assert "first_name" in user
        assert user["full_name"].startswith(user["first_name"])
