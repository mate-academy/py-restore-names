from app.restore_names import restore_names


def test_restore_names_with_empty_users_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
    ]


def test_restore_names_with_full_name_containing_extra_spaces() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "  John   Doe  ",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": " Jane    Smith ",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "  John   Doe  ",
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": " Jane    Smith ",
        },
    ]
