from app.restore_names import restore_names


def test_should_restore_first_name_when_it_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_should_restore_first_name_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_should_not_change_first_name_when_it_is_filled() -> None:
    users = [
        {
            "first_name": "Mike",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_should_not_fail_when_users_list_is_empty() -> None:
    users = []

    restore_names(users)

    assert users == []
