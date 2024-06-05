from app.restore_names import restore_names


def test_none_first_name_attribute() -> None:
    given_users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(given_users)

    assert given_users == expected_users


def test_missed_first_name_attribute() -> None:
    given_users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(given_users)

    assert given_users == expected_users
