from app import restore_names


def test_first_name_is_restored_when_it_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_first_name_is_restored_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_existing_first_name_is_not_changed() -> None:
    users = [
        {
            "first_name": "Johnny",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Johnny",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]


def test_function_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    assert restore_names.restore_names(users) is None


def test_empty_list_stays_empty() -> None:
    users = []

    restore_names.restore_names(users)

    assert users == []


def test_names_are_restored_only_for_users_who_need_it() -> None:
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
            "first_name": "Johnny",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
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
            "first_name": "Johnny",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]
