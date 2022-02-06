from app.restore_names import restore_names


def test_first_name_is_none():
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "John Black",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_no_first_name_key_in_user_dict():
    users = [
        {
            "last_name": "Jobs",
            "full_name": "Steve Jobs",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Steve"


def test_first_name_exists_in_user_dict_and_it_is_correct():
    users = [
        {
            "first_name": "Adam",
            "last_name": "Groff",
            "full_name": "Adam Groff",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Adam"
