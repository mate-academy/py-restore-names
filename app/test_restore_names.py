from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
        {"first_name": "Jane",
         "last_name": "Smith",
         "full_name": "Jane Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"


def test_restore_names_with_first_name_in_full_name() -> None:
    users = [
        {"first_name": None,
         "last_name": "Smith",
         "full_name": "Michael Smith"},
        {"first_name": None,
         "last_name": "Lee",
         "full_name": "Anna Lee"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Michael"
    assert users[1]["first_name"] == "Anna"


def test_restore_names_with_edge_case_empty_full_name() -> None:
    users = [
        {"first_name": None,
         "last_name": "Unknown",
         "full_name": ""},
        {"first_name": None,
         "last_name": "NoName",
         "full_name": ""},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Unknown"
    assert users[1]["first_name"] == "Unknown"


def test_restore_names_with_multiple_words_in_full_name() -> None:
    users = [
        {"first_name": None,
         "last_name": "Johnston",
         "full_name": "Mary Ann Johnston"},
        {"first_name": None,
         "last_name": "Doe",
         "full_name": "James Michael Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mary"
    assert users[1]["first_name"] == "James"


def test_restore_names_with_no_last_name() -> None:
    users = [
        {"first_name": None, "last_name": None, "full_name": "Alice"},
        {"first_name": None, "last_name": None, "full_name": "Bob"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
