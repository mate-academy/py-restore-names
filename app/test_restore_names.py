from .restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_first_name_present() -> None:
    users = [
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"}
    ]
    restore_names(users)
    assert users == [
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"}
    ]


def test_multiple_word_names() -> None:
    users = [
        {"first_name": None,
         "last_name": "Watson",
         "full_name": "Mary Jane Watson"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Mary",
         "last_name": "Watson",
         "full_name": "Mary Jane Watson"}
    ]


def test_no_first_name_key() -> None:
    users = [
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"}
    ]
