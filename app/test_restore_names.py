def test_restore_names_with_none_first_name() -> None:
    from app import restore_names

    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]

    result = restore_names.restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]


def test_restore_names_with_missing_first_name() -> None:
    from app import restore_names

    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    result = restore_names.restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_names_does_not_change_existing_first_name() -> None:
    from app import restore_names

    users = [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]

    result = restore_names.restore_names(users)

    assert result is None
    assert users == [
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]


def test_restore_names_with_empty_list() -> None:
    from app import restore_names

    users = []

    result = restore_names.restore_names(users)

    assert result is None
    assert users == []
