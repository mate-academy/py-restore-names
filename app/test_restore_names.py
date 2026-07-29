from app.restore_names import restore_names


def test_restore_names_updates_missing_first_names() -> None:
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

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_does_not_update_existing_first_names() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "full_name": "Alice Johnson",
        },
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
