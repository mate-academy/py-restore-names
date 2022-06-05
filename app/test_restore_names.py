from app.restore_names import restore_names


def test_add_firstname_when_firstname_is_missing():
    user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(user)

    full_user = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]

    assert user == full_user


def test_add_firstname_when_firstname_is_none():
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(user)

    full_user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    assert user == full_user
