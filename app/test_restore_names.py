from app.restore_names import restore_names


def test_users_first_name_is_equal_to_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)

    assert users[0]["first_name"] == "Jack", (
        "First name not restored correctly"
    )


def test_user_dont_have_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    expected_result = {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"
    }

    assert users[0] == expected_result, "User fields not updated correctly"
