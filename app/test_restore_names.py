from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
    ]


def test_restore_names_when_first_name_exists() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith"
        },
        {
            "first_name": "Bob",
            "last_name": "Brown",
            "full_name": "Bob Brown"
        },
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_missing_first_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "White",
            "full_name": "Tom White"
        },
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Ann Black"
        },
        {
            "first_name": None,
            "last_name": "Grey",
            "full_name": "Sam Grey"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Tom",
            "last_name": "White",
            "full_name": "Tom White"
        },
        {
            "first_name": "Ann",
            "last_name": "Black",
            "full_name": "Ann Black"
        },
        {
            "first_name": "Sam",
            "last_name": "Grey",
            "full_name": "Sam Grey"
        },
    ]


def test_restore_names_first_name_key_missing() -> None:
    users = [
        {
            "last_name": "Stone",
            "full_name": "Lily Stone"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Lily",
            "last_name": "Stone",
            "full_name": "Lily Stone"
        },
    ]


def test_restore_names_full_name_single_word() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Unknown",
            "full_name": "Mystery"
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mystery",
            "last_name": "Unknown",
            "full_name": "Mystery"
        },
    ]
