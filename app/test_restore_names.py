from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    """Test that users with first_name=None get it restored from full_name."""
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"


def test_restore_names_without_first_name_key() -> None:
    """Test that users without first_name key get it added from full_name."""
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"


def test_restore_names_preserves_existing_first_name() -> None:
    """Test that users with existing first_name are not modified."""
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]
    expected_first_name = users[0]["first_name"]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name
    assert users[0]["last_name"] == "Doe"
    assert users[0]["full_name"] == "John Doe"


def test_restore_names_example_from_readme() -> None:
    """Test the example case from README."""
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
    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"
    assert users[1]["first_name"] == "Mike"
    assert users[1]["last_name"] == "Adams"
    assert users[1]["full_name"] == "Mike Adams"


def test_restore_names_mixed_scenarios() -> None:
    """Test mixed scenarios with multiple users."""
    users = [
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Bob Brown",
        },
        {
            "last_name": "White",
            "full_name": "Alice White",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jane"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Alice"


def test_restore_names_returns_none() -> None:
    """Test that function returns None (modifies in place)."""
    users = [
        {
            "first_name": None,
            "full_name": "Test User",
        },
    ]
    result = restore_names(users)
    assert result is None
