import pytest
from app.restore_names import restore_names
from typing import List, Dict


@pytest.fixture
def example_users() -> List[Dict[str, str]]:
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


def test_restore_names_sets_correct_first_names(example_users: List[Dict[str, str]]) -> None: # Noqa E501
    restore_names(example_users)
    assert example_users == [
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


def test_restore_names_does_not_override_existing_first_names(example_users: List[Dict[str, str]]) -> None: # Noqa E501
    # Add an existing first name
    example_users[0]["first_name"] = "John"
    restore_names(example_users)
    assert example_users == [
        {
            "first_name": "John",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_names_does_not_override_nonempty_first_names(example_users: List[Dict[str, str]]) -> None: # Noqa E501
    # Add a non-empty first name
    example_users[0]["first_name"] = "John"
    restore_names(example_users)
    assert example_users == [
        {
            "first_name": "John",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
