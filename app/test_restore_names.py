from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Emily",
            "last_name": "Smith",
            "full_name": "Emily Smith",
        },
        {"first_name": None, "last_name": "Brown", "full_name": "Chris Brown"},
    ]

    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Emily",
            "last_name": "Smith",
            "full_name": "Emily Smith",
        },
        {
            "first_name": "Chris",
            "last_name": "Brown",
            "full_name": "Chris Brown"
        },
    ]

    restore_names(users)
    assert users == expected


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_no_changes_needed() -> None:
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "full_name": "Alice Johnson",
        },
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected
