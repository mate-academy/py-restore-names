import pytest
from app.restore_names import restore_names

def test_restore_names_basic():
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},  # Ключа нет
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},  # Ключ None
        {"first_name": "Alice", "full_name": "Alice Wonderland"}  # Уже есть
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Alice"  # Не изменилось


def test_restore_names_single_name():
    users = [{"full_name": "Beyonce"}]
    restore_names(users)
    assert users[0]["first_name"] == "Beyonce"


def test_restore_names_extra_spaces():
    users = [{"full_name": "  Leonhard   Euler  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Leonhard"


def test_restore_names_empty_list():
    users = []
    restore_names(users)
    assert users == []
