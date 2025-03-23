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
    {
        "first_name": "Monica",
        "last_name": "Geller",
        "full_name": "Monica Geller",
    },
]


def test_restore_names_correctly_change_names() -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
