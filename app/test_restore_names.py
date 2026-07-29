from app.restore_names import restore_names


def test_should_restore_name_if_name_none() -> None:
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


def test_should_restore_name_if_name_not_exist() -> None:
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

    assert users[1]["first_name"] == "Mike"


def test_should_do_nothing_if_name_exist() -> None:
    users = [
        {
            "first_name": "Jack-test",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack-test"
