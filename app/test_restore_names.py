from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
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
    ]

    expected = [
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

    restore_names(users)
    assert users == expected


def test_restore_names_with_existing_first_name() -> None:
    users = [
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

    expected = [
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

    restore_names(users)
    assert users == expected


def test_restore_names_with_empty_list() -> None:
    users = []
    expected = []

    restore_names(users)
    assert users == expected


def test_restore_names_with_partial_missing_first_name() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        },
    ]

    expected = [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
        {
            "first_name": "Charlie",
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        },
    ]

    restore_names(users)
    assert users == expected
