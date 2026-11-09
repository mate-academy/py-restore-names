from app.restore_names import restore_names


def test_restore_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_keep_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_for_multiple_users() -> None:
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
            "full_name": "John Smith",
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
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]


def test_empty_users_list() -> None:
    users = []

    result = restore_names(users)

    assert result is None
    assert users == []
