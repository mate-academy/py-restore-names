import pytest
from app.restore_names import restore_names


def test_restore_missing_first_name() -> None:
    """Test restoring first_name when it is None."""
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
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


def test_keep_existing_first_name() -> None:
    """Test that existing first_name values remain unchanged."""
    users = [
        {
            "first_name": "Anna",
            "last_name": "Stone",
            "full_name": "Anna Stone",
        },
        {
            "first_name": "Bob",
            "last_name": "Miller",
            "full_name": "Bob Miller",
        },
    ]

    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_mixed_first_name_presence() -> None:
    """Test mix of users with and without first_name."""
    users = [
        {
            "first_name": "Tom",
            "last_name": "Hill",
            "full_name": "Tom Hill",
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
        {
            "last_name": "Fox",
            "full_name": "Alice Fox",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Tom"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Alice"


def test_empty_user_list() -> None:
    """Test behavior with an empty user list (no changes)."""
    users: list[dict] = []
    restore_names(users)
    assert users == []


@pytest.mark.parametrize(
    "full_name, expected_first",
    [
        ("John Smith", "John"),
        ("Eva Brown", "Eva"),
        ("X Æ", "X"),
        ("  Alice Cooper  ", "Alice"),
    ],
)
def test_first_name_extraction(
    full_name: str,
    expected_first: str,
) -> None:
    """Test that first_name is correctly extracted from full_name."""
    users = [{"last_name": "Test", "full_name": full_name}]
    restore_names(users)
    assert users[0]["first_name"] == expected_first
