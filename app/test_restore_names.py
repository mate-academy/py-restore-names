from app.restore_names import restore_names


def test_some_first_names_are_missing() -> None:
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
        {
            "first_name": "Igor",
            "last_name": "Shevchenko",
            "full_name": "Igor Shevchenko",
        }
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
        {
            "first_name": "Igor",
            "last_name": "Shevchenko",
            "full_name": "Igor Shevchenko",
        }
    ]

    restore_names(users)

    assert users == expected_users


def test_every_user_has_no_first_name() -> None:
    users = [
        {
            "last_name": "Smith",
            "full_name": "Alex Smith",
        },
        {
            "last_name": "Black",
            "full_name": "Charlie Black",
        }
    ]

    expected_users = [
        {
            "first_name": "Alex",
            "last_name": "Smith",
            "full_name": "Alex Smith",
        },
        {
            "first_name": "Charlie",
            "last_name": "Black",
            "full_name": "Charlie Black",
        }
    ]

    restore_names(users)

    assert users == expected_users


def test_first_name_already_exists() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"


def test_full_name_has_extra_spaces() -> None:
    users = [
        {
            "last_name": "Shevchenko",
            "full_name": "    Igor        Shevchenko",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Igor"


def test_full_name_has_more_than_one_word() -> None:
    users = [
        {
            "last_name": "Michael Doe",
            "full_name": "John Michael Doe",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_list_of_users_is_empty() -> None:
    users = []
    restore_names(users)
    assert users == []
