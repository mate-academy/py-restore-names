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
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "Michael Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_multiple_users_mixed_cases() -> None:
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
            "first_name": "Existing",
            "last_name": "Brown",
            "full_name": "Should Not Change",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Existing"


def test_function_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
