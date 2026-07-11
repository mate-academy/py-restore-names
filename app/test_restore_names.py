from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    restore_names(users)

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


def test_restore_names_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]


def test_restore_names_should_not_change_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []
