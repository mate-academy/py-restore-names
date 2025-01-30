import pytest
from app.restore_names import restore_names
from typing import List, Dict, Optional


@pytest.fixture
def sample_users() -> List[Dict[str, Optional[str]]]:
    return [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


@pytest.fixture
def unchanged_users() -> List[Dict[str, Optional[str]]]:
    return [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
    ]


@pytest.fixture
def missing_full_name_users() -> List[Dict[str, Optional[str]]]:
    return [
        {"first_name": None,
         "last_name": "Brown",
         "full_name": "Unknown Brown"},
        {"last_name": "Taylor",
         "full_name": "Emma Taylor"},
    ]


def test_restore_names_basic(sample_users: list) -> None:
    restore_names(sample_users)
    expected = [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    assert sample_users == expected


def test_restore_names_no_change(unchanged_users: list) -> None:
    original = unchanged_users.copy()
    restore_names(unchanged_users)
    assert unchanged_users == original


def test_restore_names_missing_full_name(
        missing_full_name_users: list) -> None:
    restore_names(missing_full_name_users)
    expected = [
        {"first_name": "Unknown",
         "last_name": "Brown",
         "full_name": "Unknown Brown"},
        {"first_name": "Emma",
         "last_name": "Taylor",
         "full_name": "Emma Taylor"},
    ]
    assert missing_full_name_users == expected


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_spaces() -> None:
    users = [
        {"first_name": None,
         "last_name": "Lee",
         "full_name": "   Tom   Lee   "},
    ]
    restore_names(users)
    expected = [
        {"first_name": "Tom",
         "last_name": "Lee",
         "full_name": "   Tom   Lee   "},
    ]
    assert users == expected
