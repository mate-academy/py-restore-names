from app import restore_names


def test_none_as_first_name() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Mike Adams",
        }
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_first_name_is_missing() -> None:
    users = [
        {
            "full_name": "Mike Adams",
        }
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_first_name_already_exists() -> None:
    users = [
        {
            "first_name": "John",
            "full_name": "Mike Adams",
        }
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "John"
