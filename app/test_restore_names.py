from app.restore_names import restore_names


def test_restore_first_name_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_when_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_keep_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_multiple_users() -> None:
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


def test_restore_names_returns_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]

    result = restore_names(users)

    assert result is None


def test_empty_users_list() -> None:
    users = []

    result = restore_names(users)

    assert users == []
    assert result is None
