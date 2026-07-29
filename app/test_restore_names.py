import app.restore_names as restore_names_module


def test_restore_first_name_when_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names_module.restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_restore_first_name_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names_module.restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_do_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Brown",
            "full_name": "Anna Brown",
        }
    ]

    restore_names_module.restore_names(users)

    assert users[0]["first_name"] == "Anna"


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
        {
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sara Connor",
        },
    ]

    restore_names_module.restore_names(users)

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
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sara Connor",
        },
    ]


def test_function_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names_module.restore_names(users)

    assert result is None
