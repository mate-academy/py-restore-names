import pytest
from app.restore_names import restore_names


def test_restore_names_basic() -> None:
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


def test_restore_names_already_present() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown",
        },
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown",
        },
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "full_name": "Bob Smith",
        },
    ]


def test_restore_names_missing_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Doe"},  # Без full_name
        {"last_name": "White", "full_name": "John White"},
    ]

    with pytest.raises(KeyError, match="'full_name'"):
        restore_names(users)
