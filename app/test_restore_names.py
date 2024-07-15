from app.restore_names import restore_names


def test_first_name_is_equal_to_none() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(user)

    expected_user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    assert user == expected_user


def test_missing_first_name() -> None:
    user = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(user)

    expected_user = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    assert user == expected_user
