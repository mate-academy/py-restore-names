from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
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
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
    ]

    expected = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
    ]

    restore_names(users)
    assert users == expected


def test_restore_names_missing_first_name_key() -> None:
    users = [
        {
            "last_name": "Johnson",
            "full_name": "Michael Johnson",
        },
        {
            "first_name": "Emma",
            "last_name": "Stone",
            "full_name": "Emma Stone",
        },
    ]

    expected = [
        {
            "first_name": "Michael",
            "last_name": "Johnson",
            "full_name": "Michael Johnson",
        },
        {
            "first_name": "Emma",
            "last_name": "Stone",
            "full_name": "Emma Stone",
        },
    ]

    restore_names(users)
    assert users == expected


def test_restore_names_empty_list() -> None:
    users = []
    expected = []

    restore_names(users)
    assert users == expected


def test_restore_names_single_word_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "",
            "full_name": "Madonna",
        }
    ]

    expected = [
        {
            "first_name": "Madonna",
            "last_name": "",
            "full_name": "Madonna",
        }
    ]

    restore_names(users)
    assert users == expected
