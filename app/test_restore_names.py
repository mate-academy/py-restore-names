from app.restore_names import restore_names


def test_restore_name_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_name_when_first_name_is_missing() -> None:
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
            "full_name": "Mike Adams",
        }
    ]


def test_do_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Kate",
            "last_name": "Brown",
            "full_name": "Katherine Brown",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Kate",
            "last_name": "Brown",
            "full_name": "Katherine Brown",
        }
    ]
