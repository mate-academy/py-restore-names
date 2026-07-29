from app.restore_names import restore_names


def test_restore_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_when_first_name_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_do_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "Existing",
            "last_name": "User",
            "full_name": "New Name",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Existing"


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
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_full_name_with_multiple_parts() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Michael Doe",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_empty_full_name_should_not_crash() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "",
        }
    ]

    restore_names(users)

    assert users[0].get("first_name") is None


def test_missing_full_name_should_not_crash() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
        }
    ]

    restore_names(users)

    assert users[0].get("first_name") is None


def test_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None


def test_mutates_original_list() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    original = users

    restore_names(users)

    assert users is original
