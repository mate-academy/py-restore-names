from app.restore_names import restore_names


def test_restore_names_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    assert users == expected


def test_restore_names_does_not_change_existing_first_name() -> None:
    users = [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
    ]
    assert users == expected


def test_restore_names_partial_data() -> None:
    users = [
        {"first_name": None, "full_name": "Bob Brown"},
        {"first_name": None, "last_name": "Wilson",
         "full_name": "Sam Wilson"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Bob"
    assert users[1]["first_name"] == "Sam"
