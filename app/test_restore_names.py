from app.restore_names import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_do_not_overwrite_existing_first_name() -> None:
    users = [
        {
            "first_name": "AlreadySet",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "AlreadySet"


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Wonderland"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charlie Brown"}
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"
