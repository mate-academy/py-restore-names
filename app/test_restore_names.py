from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_restore_with_existing_first_name() -> None:
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": None, "last_name": "Smith", "full_name": "Jane Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"  # existing should remain
    assert users[1]["first_name"] == "Jane"  # missing restored


def test_restore_all_missing() -> None:
    users = [
        {"last_name": "Brown", "full_name": "Charlie Brown"},
        {"first_name": None, "last_name": "White", "full_name": "Lucy White"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Charlie"
    assert users[1]["first_name"] == "Lucy"


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_full_name_with_multiple_words() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "King",
            "full_name": "Martin Luther King",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Martin"
