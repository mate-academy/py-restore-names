from app.restore_names import restore_names


def test_restore_name_when_first_name_is_none() -> None:
    """Test restoring first name when it's None"""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users == expected


def test_restore_name_when_first_name_missing() -> None:
    """Test restoring first name when it's not in dict"""
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    expected = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users == expected


def test_no_change_when_first_name_exists() -> None:
    """Test no modification when first_name already exists"""
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe"
        }
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_multiple_users_mixed_cases() -> None:
    """Test multiple users with various conditions"""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith"
        }
    ]
    expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith"
        }
    ]
    restore_names(users)
    assert users == expected


def test_empty_users_list() -> None:
    """Test with empty list"""
    users = []
    expected = []
    restore_names(users)
    assert users == expected


def test_single_word_full_name() -> None:
    """Test with full_name containing only one word"""
    users = [
        {
            "first_name": None,
            "last_name": "Unknown",
            "full_name": "John"
        }
    ]
    expected = [
        {
            "first_name": "John",
            "last_name": "Unknown",
            "full_name": "John"
        }
    ]
    restore_names(users)
    assert users == expected
