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

    restore_names(users)

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
    ]


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
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
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]


def test_restore_names_with_multiple_words_in_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "King",
            "full_name": "Martin Luther King",
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Chris Brown",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Martin",
            "last_name": "King",
            "full_name": "Martin Luther King",
        },
        {
            "first_name": "Chris",
            "last_name": "Brown",
            "full_name": "Chris Brown",
        },
    ]


def test_restore_names_no_change_needed() -> None:
    users = [
        {
            "first_name": "Bill",
            "last_name": "Gates",
            "full_name": "Bill Gates",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Bill",
            "last_name": "Gates",
            "full_name": "Bill Gates",
        },
    ]
