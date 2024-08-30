from app.restore_names import restore_names


def test_should_restore_name() -> None:
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
    for i in users:
        assert i["first_name"] == i["full_name"].split()[0]
