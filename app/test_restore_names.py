from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
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
    assert users == expected, f"Expected {expected}, but got {users}"


def test_restore_names_missing_first_name_field() -> None:
    users = [
        {
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "last_name": "Brown",
            "full_name": "John Brown",
        },
    ]
    restore_names(users)
    expected = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "first_name": "John",
            "last_name": "Brown",
            "full_name": "John Brown",
        },
    ]
    assert users == expected, f"Expected {expected}, but got {users}"


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "Emily",
            "last_name": "Stone",
            "full_name": "Emily Stone",
        },
        {
            "first_name": "Chris",
            "last_name": "Evans",
            "full_name": "Chris Evans",
        },
    ]
    restore_names(users)
    expected = [
        {
            "first_name": "Emily",
            "last_name": "Stone",
            "full_name": "Emily Stone",
        },
        {
            "first_name": "Chris",
            "last_name": "Evans",
            "full_name": "Chris Evans",
        },
    ]
    assert users == expected, f"Expected {expected}, but got {users}"


def test_restore_names_with_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == [], "Expected an empty list, but got a modified list"


def test_restore_names_with_incorrect_full_name_format() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Unknown",
            "full_name": "OnlyOneName",
        },
    ]
    restore_names(users)
    expected = [
        {
            "first_name": "OnlyOneName",
            "last_name": "Unknown",
            "full_name": "OnlyOneName",
        },
    ]
    assert users == expected, f"Expected {expected}, but got {users}"
