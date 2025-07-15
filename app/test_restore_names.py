import pytest
from app.restore_names import restore_names


def test_restore_names_sets_first_name_if_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Anna"


def test_restore_names_sets_first_name_if_missing() -> None:
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Linda", "last_name": "Brown", "full_name": "Linda Brown"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
    assert users[1]["first_name"] == "Linda"


def test_restore_names_does_not_change_existing_first_name() -> None:
    users = [
        {"first_name": "Tom", "last_name": "Green", "full_name": "Tom Green"},
        {"first_name": None, "last_name": "White", "full_name": "Sam White"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Tom"
    assert users[1]["first_name"] == "Sam"


def test_restore_names_handles_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_single_name_in_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "", "full_name": "Cher"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Cher"
