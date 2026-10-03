from app.restore_names import restore_names


def test_should_restore_first_name_when_it_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_should_restore_first_name_when_it_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Michael Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_should_restore_names_for_multiple_users() -> None:
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
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Michael Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "John"
