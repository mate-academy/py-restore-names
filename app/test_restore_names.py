from app.restore_names import restore_names


def test_restore_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_when_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_do_not_override_existing() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Snow",
            "full_name": "John Snow",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_multiple_users() -> None:
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
        {
            "first_name": "Anna",
            "last_name": "Taylor",
            "full_name": "Anna Taylor",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Anna",
            "last_name": "Taylor",
            "full_name": "Anna Taylor",
        },
    ]
