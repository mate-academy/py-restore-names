import pytest
from app.restore_names import restore_names


def test_none_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    expected = [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == expected


def test_missing_first_name() -> None:
    users = [
        {"last_name": "Doe", "full_name": "John Doe"},
    ]
    expected = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == expected


def test_valid_first_name() -> None:
    users = [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
    ]
    expected = [
        {"first_name": "Alice",
         "last_name": "Smith",
         "full_name": "Alice Smith"},
    ]
    restore_names(users)
    assert users == expected


def test_multiple_spaces_in_full_name() -> None:
    users = [
        {"last_name": "Brown", "full_name": "  Charlie   Brown  "},
    ]
    expected = [
        {"first_name": "Charlie",
         "last_name": "Brown",
         "full_name": "  Charlie   Brown  "},
    ]
    restore_names(users)
    assert users == expected


def test_empty_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Doe", "full_name": ""},
    ]
    expected = [
        {"first_name": None, "last_name": "Doe", "full_name": ""},
    ]
    restore_names(users)
    assert users == expected


def test_missing_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Doe"},
    ]
    with pytest.raises(KeyError):
        restore_names(users)
