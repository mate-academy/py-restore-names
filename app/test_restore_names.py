from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Doe", "full_name": "John Doe"},
        {"last_name": "Smith", "full_name": "Alice Smith"},
    ]
    expected = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Alice", "last_name": "Smith",
         "full_name": "Alice Smith"},
    ]
    restore_names(users)
    assert users == expected


def test_restore_does_nothing_if_first_name_exists() -> None:
    users = [
        {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"},
    ]
    expected = [
        {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users == expected


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_partial_data() -> None:
    users = [
        {"full_name": "Tom Sawyer"},
        {"first_name": None, "full_name": "Huck Finn"},
    ]
    expected = [
        {"first_name": "Tom", "full_name": "Tom Sawyer"},
        {"first_name": "Huck", "full_name": "Huck Finn"},
    ]
    restore_names(users)
    for user, exp in zip(users, expected):
        for key in exp:
            assert user[key] == exp[key]
