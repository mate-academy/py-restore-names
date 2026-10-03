from app.restore_names import restore_names


def test_can_sum() -> None:
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

    assert (
        all([
            user.get("first_name", False)
            for user in users
        ]) is True
    ), "All users must have a full name"
