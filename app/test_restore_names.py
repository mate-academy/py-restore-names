from app import restore_names


def test_restore_names_when_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Parker",
            "full_name": "Peter Parker",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Peter",
            "last_name": "Parker",
            "full_name": "Peter Parker",
        }
    ]


def test_restore_names_when_first_name_is_missing() -> None:
    users = [
        {
            "last_name": "Stark",
            "full_name": "Tony Stark",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Tony",
            "last_name": "Stark",
            "full_name": "Tony Stark",
        }
    ]


def test_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Steven",
            "last_name": "Strange",
            "full_name": "Steven Strange",
        }
    ]
    restore_names.restore_names(users)
    assert users == [
        {
            "first_name": "Steven",
            "last_name": "Strange",
            "full_name": "Steven Strange",
        }
    ]
