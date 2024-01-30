import pytest
from typing import List, Dict

from app.restore_names import restore_names


@pytest.fixture
def users_with_missing_first_name() -> List[Dict[str, str]]:
    return [
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


def test_restore_names_with_missing_first_name(
        users_with_missing_first_name: List[Dict[str, str]]
) -> None:
    users = users_with_missing_first_name.copy()

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


@pytest.fixture
def users_with_existing_first_name() -> List[Dict[str, str]]:
    return [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
    ]


def test_restore_names_with_existing_first_name(
        users_with_existing_first_name: List[Dict[str, str]]
) -> None:
    users = users_with_existing_first_name.copy()

    restore_names(users)

    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
    ]


def test_restore_names_with_empty_list() -> None:
    users: List[Dict[str, str]] = []
    restore_names(users)
    assert users == []
