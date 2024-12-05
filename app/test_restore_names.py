from typing import List

import pytest

from app.restore_names import restore_names


def test_no_change_if_first_name_exists() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Smith", "full_name":
            "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    expected_users = users.copy()
    restore_names(users)
    assert users == expected_users


def test_empty_user_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_with_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Anna Smith",
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
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
    ]


def test_restore_names_with_missing_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sara Connor",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Sara",
            "last_name": "Connor",
            "full_name": "Sara Connor",
        },
    ]


def test_restore_names_with_complete_data() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
    ]
