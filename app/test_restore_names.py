from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_restore_absent_first_name_key() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"


def test_do_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Sarah"


def test_restore_multiple_users() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "Anna",
         "last_name": "Brown",
         "full_name": "Anna Brown"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Anna"
