from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    """Test restoring first name when it's None"""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"


def test_restore_names_with_missing_first_name() -> None:
    """Test restoring first name when the key doesn't exist"""
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mike"
    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"


def test_restore_names_example_from_readme() -> None:
    """Test the exact example from README"""
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

    expected_users = [
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

    assert users == expected_users


def test_restore_names_with_existing_first_name() -> None:
    """Test that existing first names are not modified"""
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"


def test_restore_names_multiple_users_mixed() -> None:
    """Test with multiple users having different scenarios"""
    users = [
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": None,
            "last_name": "Johnson",
            "full_name": "Bob Johnson",
        },
        {
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alice"  # unchanged
    assert users[1]["first_name"] == "Bob"    # restored from None
    assert users[2]["first_name"] == "Charlie"  # restored from missing


def test_restore_names_with_single_name() -> None:
    """Test with full name containing only one name"""
    users = [
        {
            "first_name": None,
            "last_name": "",
            "full_name": "Madonna",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Madonna"


def test_restore_names_with_multiple_names() -> None:
    """Test with full name containing multiple names"""
    users = [
        {
            "first_name": None,
            "last_name": "Van Der Berg",
            "full_name": "Anna Van Der Berg",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Anna"


def test_restore_names_empty_list() -> None:
    """Test with empty list of users"""
    users = []

    restore_names(users)

    assert users == []


def test_restore_names_returns_none() -> None:
    """Test that function returns None (modifies in place)"""
    users = [
        {
            "first_name": None,
            "last_name": "Test",
            "full_name": "John Test",
        }
    ]

    result = restore_names(users)

    assert result is None
    assert users[0]["first_name"] == "John"


def test_restore_names_with_hyphenated_first_name() -> None:
    """Test with hyphenated first name"""
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Mary-Jane Smith",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Mary-Jane"


def test_restore_names_with_prefixed_name() -> None:
    """Test with name prefixes like Dr., Mr., etc."""
    users = [
        {
            "first_name": None,
            "last_name": "Watson",
            "full_name": "Dr. John Watson",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Dr."
