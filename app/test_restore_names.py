from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Shulzhenko",
            "full_name": "Oles Shulzhenko"
        },
        {
            "last_name": "Academy",
            "full_name": "Mate Academy"
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Oles",
            "last_name": "Shulzhenko",
            "full_name": "Oles Shulzhenko"
        },
        {
            "first_name": "Mate",
            "last_name": "Academy",
            "full_name": "Mate Academy"
        }
    ]
