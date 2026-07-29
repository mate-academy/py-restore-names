from app.restore_names import restore_names


def test_restore_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    expected_result = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
            "first_name": "Mike"
        }
    ]

    restore_names(users)
    assert users == expected_result


def test_restore_users_when_empty() -> None:
    users = []
    restore_names(users)
    assert users == []
