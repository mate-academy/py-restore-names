from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [{"last_name": "Adams", "full_name": "Mike Adams"}]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_keep_existing_first_name() -> None:
    users = [{"first_name": "John", "full_name": "John Smith"}]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_empty_users() -> None:
    users = []

    result = restore_names(users)

    assert result is None
    assert users == []
