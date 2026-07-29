from app.restore_names import restore_names


def test_restore_names_with_missing_or_none_first_name() -> None:
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


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
