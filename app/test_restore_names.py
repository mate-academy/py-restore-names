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
    assert (
        users[0]["first_name"] == "Jack"
        and users[1]["first_name"] == "Mike"
    ), "First user first name should be 'Jack'"
