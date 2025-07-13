import pytest

from app import restore_names  # або імпортуйте звідти, де у вас функція

def test_restore_names_basic():
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Alice"  # має лишитись незмінним

def test_restore_names_empty_list():
    users = []
    restore_names(users)
    assert users == []

def test_restore_names_already_filled():
    users = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Jane", "last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"

def test_restore_names_missing_full_name():
    users = [
        {"first_name": None, "last_name": "Unknown"},
        {"last_name": "Unknown"},
    ]
    # Якщо full_name відсутній, first_name не змінюємо
    restore_names(users)
    assert users[0].get("first_name") is None
    assert "first_name" not in users[1]

def test_restore_names_full_name_with_multiple_words():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Michael Smith"},
    ]
    restore_names(users)
    # Маємо взяти перше слово full_name як first_name
    assert users[0]["first_name"] == "John"
