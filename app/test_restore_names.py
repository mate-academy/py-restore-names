from app.restore_names import restore_names


def test_restore_names_should_update_missing_or_none_names() -> None:
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


def test_restore_names_should_not_overwrite_existing_names() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Swift",
            "full_name": "Alice Swift",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alice"


def test_restore_names_returns_none() -> None:
    users = [{"last_name": "Doe", "full_name": "John Doe"}]
    assert restore_names(users) is None
