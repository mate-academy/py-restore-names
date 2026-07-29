from app.restore_names import restore_names


users_expected = [
    {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }
]


def test_restore_names_firstname_equal_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == users_expected


def test_restore_names_without_firstname() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users == users_expected
