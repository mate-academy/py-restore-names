from app.restore_names import restore_names


def test_restore_names_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name":
            "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name":
            "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack", "last_name":
            "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name":
            "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names_existing_first_name() -> None:
    users = [
        {"first_name": "Anna", "last_name":
            "Smith", "full_name": "Anna Smith"},
        {"first_name": "John", "last_name":
            "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Anna", "last_name":
            "Smith", "full_name": "Anna Smith"},
        {"first_name": "John", "last_name":
            "Doe", "full_name": "John Doe"},
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_mixed_cases() -> None:
    users = [
        {"first_name": None, "last_name":
            "Brown", "full_name": "Chris Brown"},
        {"first_name": "Sarah", "last_name":
            "Connor", "full_name": "Sarah Connor"},
        {"last_name": "White", "full_name":
            "Lucy White"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Chris", "last_name":
            "Brown", "full_name": "Chris Brown"},
        {"first_name": "Sarah", "last_name":
            "Connor", "full_name": "Sarah Connor"},
        {"first_name": "Lucy", "last_name":
            "White", "full_name": "Lucy White"},
    ]
