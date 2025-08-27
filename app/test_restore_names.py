import pytest
from app.main import restore_names  # Certifique-se de ter __init__.py em app/

def test_restore_first_name_none():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_first_name_missing_key():
    users = [
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_does_not_override_existing_first_name():
    users = [
        {"first_name": "Anna", "last_name": "Smith", "full_name": "Anna Smith"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Anna"  # não deve mudar


def test_multiple_users_restoration():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Sara", "last_name": "Connor", "full_name": "Sara Connor"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Sara"


def test_full_name_single_word():
    users = [
        {"first_name": None, "full_name": "Plato"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Plato"
