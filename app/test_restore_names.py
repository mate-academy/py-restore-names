from app.restore_names import restore_names


def test_function_with_users_whose_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_function_with_users_whose_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_function_with_users_whose_first_name_is() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
