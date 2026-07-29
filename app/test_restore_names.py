from app.restore_names import restore_names


def test_restore_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Kiporenko",
            "full_name": "Maxym Kiporenko"
        },
        {
            "last_name": "Pustovit",
            "full_name": "Natalia Pustovit"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Maxym"
    assert users[1]["first_name"] == "Natalia"
