from app.restore_names import restore_names


def test_restore_names_with_missing_and_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
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


def test_restore_names_with_valid_first_name() -> None:
    users = [
        {
            "first_name": "Lily",
            "last_name": "Smith",
            "full_name": "Lily Smith",
        }
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_partial_keys() -> None:
    users = [
        {"first_name": None, "full_name": "Anna Bell"},
        {"full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Anna", "full_name": "Anna Bell"},
        {"first_name": "John", "full_name": "John Doe"},
    ]
