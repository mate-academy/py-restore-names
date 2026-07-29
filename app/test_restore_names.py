from app.restore_names import restore_names


def test_restore_name_with_user_whose_1st_name_is_none_or_missing() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Small",
            "full_name": "Biggy Small",
        },
        {
            "last_name": "Duda",
            "full_name": "Andrzej Duda",
        }
    ]

    restored = [
        {
            "first_name": "Biggy",
            "last_name": "Small",
            "full_name": "Biggy Small",
        },
        {
            "first_name": "Andrzej",
            "last_name": "Duda",
            "full_name": "Andrzej Duda",
        }
    ]

    restore_names(users)
    assert users == restored
