from app import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "John"
