from app.restore_names import restore_names


def test_restore_names_in_different_cases() -> None:
    users = [
        {
            "last_name": "Markize",
            "full_name": "Mark Markize",
        },
        {
            "first_name": None,
            "last_name": "Luke",
            "full_name": "Alex Luke",
        }
    ]
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
