from app.restore_names import restore_names


# test with OK list
# no first name key
# first name is None
def test_restore_names_without_firstname() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_restore_names_with_firstname_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_restore_names_with_ok_users() -> None:
    users = [
        {
            "first_name": "Ryan",
            "last_name": "Gosling",
            "full_name": "Ryan Gosling"
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Ryan",
            "last_name": "Gosling",
            "full_name": "Ryan Gosling"
        }
    ]
