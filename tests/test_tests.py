from typing import List
import pytest
from app.restore_names import restore_names


def test_restore_only_missing_names():
    users = [
        {"last_name": "Doe", "full_name": "John Doe"},
        {"first_name": None, "last_name": "Smith", "full_name": "Alice Smith"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Alice", "last_name": "Smith", "full_name": "Alice Smith"},
    ]

    assert users == expected, "The function should correctly restore missing first names"


def test_restore_only_none_names():
    users = [
        {"first_name": None, "last_name": "Taylor", "full_name": "Emma Taylor"},
        {"first_name": "", "last_name": "Brown", "full_name": "James Brown"},
    ]

    restore_names(users)

    expected = [
        {"first_name": "Emma", "last_name": "Taylor", "full_name": "Emma Taylor"},
        {"first_name": "James", "last_name": "Brown", "full_name": "James Brown"},
    ]

    assert users == expected, "The function should correctly restore names when first_name is None or empty"
