from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    result = restore_names(users)

    assert users[0]["first_name"] == "Mike"
    assert result is None


def test_restore_first_name_equal_to_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_keep_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_for_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"full_name": "Mike Adams"},
        {"first_name": "Jane", "full_name": "Jane Doe"},
    ]

    restore_names(users)

    assert [user["first_name"] for user in users] == ["Jack", "Mike", "Jane"]


def test_restore_names_with_empty_list() -> None:
    assert restore_names([]) is None
