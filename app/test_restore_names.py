from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
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


def test_preserve_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "first_name": "Bob",
            "last_name": "Jones",
            "full_name": "Bob Jones",
        },
    ]
    original = users.copy()
    restore_names(users)
    assert users == original


def test_empty_first_name_string() -> None:
    users = [
        {
            "first_name": "",
            "last_name": "Stone",
            "full_name": "Emily Stone",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Emily"


def test_full_name_with_middle_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "John Michael Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_full_name_single_word() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "",
            "full_name": "Cher",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Cher"


def test_missing_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Unknown",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] is None


def test_full_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Ghost",
            "full_name": None,
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] is None


def test_full_name_is_empty_string() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Ghost",
            "full_name": "",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == ""


def test_multiple_users_mixed_cases() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Lee",
            "full_name": "Bruce Lee",
        },
        {
            "first_name": "Alice",
            "last_name": "Wonder",
            "full_name": "Alice Wonder",
        },
        {
            "first_name": "",
            "last_name": "Bond",
            "full_name": "James Bond",
        },
        {
            "first_name": None,
            "last_name": "Solo",
            "full_name": None,
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Bruce",
            "last_name": "Lee",
            "full_name": "Bruce Lee",
        },
        {
            "first_name": "Alice",
            "last_name": "Wonder",
            "full_name": "Alice Wonder",
        },
        {
            "first_name": "James",
            "last_name": "Bond",
            "full_name": "James Bond",
        },
        {
            "first_name": None,
            "last_name": "Solo",
            "full_name": None,
        },
    ]
