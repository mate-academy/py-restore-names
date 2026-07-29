from app.restore_names import restore_names


def test_should_ignore_name_if_user_has_correct_name():
    users = [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_should_change_name_if_user_has_no_name():
    users = [
        {
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_should_change_name_if_name_is_none():
    users = [
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"
