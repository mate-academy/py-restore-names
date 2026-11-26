from app import restore_names


def test_should_restore_first_name_when_it_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Robert",
            "last_name": "Brown",
            "full_name": "Robert Brown",
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
            "first_name": "Robert",
            "last_name": "Brown",
            "full_name": "Robert Brown",
        },
    ]


def test_should_restore_first_name_when_key_is_missing() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]


def test_should_not_replace_existing_first_name() -> None:
    users = [
        {
            "first_name": "Robert",
            "last_name": "Brown",
            "full_name": "Bob Brown",
        },
    ]

    restore_names.restore_names(users)

    assert users[0]["first_name"] == "Robert"


def test_should_work_with_empty_list() -> None:
    users = []

    restore_names.restore_names(users)

    assert users == []


def test_should_return_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    result = restore_names.restore_names(users)

    assert result is None
