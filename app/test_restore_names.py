from app.restore_names import restore_names


def test_restore_only_none_names() -> None:
    users = [
        {"first_name": "", "last_name": "Brown", "full_name": "Mike Brown"},
        {"first_name": "", "last_name": "Black", "full_name": "Anna Black"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Mike", "last_name": "Brown", "full_name": "Mike Brown"},
        {"first_name": "Anna", "last_name": "Black", "full_name": "Anna Black"}
    ]


def test_restore_missing_first_name_key() -> None:
    users = [
        {"last_name": "Smith", "full_name": "John Smith"},
        {"last_name": "Taylor", "full_name": "Anna Taylor"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John", "last_name": "Smith", "full_name": "John Smith"},
        {"first_name": "Anna", "last_name": "Taylor", "full_name": "Anna Taylor"}
    ]


def test_restore_only_missing_names() -> None:
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Smith"},
        {"first_name": None, "last_name": "Taylor", "full_name": "Anna Taylor"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John", "last_name": "Smith", "full_name": "John Smith"},
        {"first_name": "Anna", "last_name": "Taylor", "full_name": "Anna Taylor"}
    ]


def test_preserve_existing_first_name() -> None:
    users = [
        {"first_name": "Emily", "last_name": "Blunt", "full_name": "Emily Blunt"},
        {"first_name": "Chris", "last_name": "Evans", "full_name": "Chris Evans"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Emily", "last_name": "Blunt", "full_name": "Emily Blunt"},
        {"first_name": "Chris", "last_name": "Evans", "full_name": "Chris Evans"}
    ]


def test_empty_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Brown", "full_name": "Jay Brown"},
        {"first_name": None, "last_name": "Black", "full_name": "Joe Black"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jay", "last_name": "Brown", "full_name": "Jay Brown"},
        {"first_name": "Joe", "last_name": "Black", "full_name": "Joe Black"}
    ]


def test_empty_users_list() -> None:
    users = []
    restore_names(users)
    assert users == []
