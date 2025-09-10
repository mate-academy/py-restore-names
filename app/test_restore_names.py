from __future__ import annotations

from typing import Dict, List, Optional, Any, Tuple
import copy
import pytest

from app.restore_names import restore_names

User = Dict[str, Any]


def test_sets_first_name_when_missing_or_none() -> None:
    users: List[User] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]

    result: Optional[None] = restore_names(users)

    # Function should return nothing (i.e., None) and mutate in place.
    assert result is None

    expected: List[User] = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    assert users == expected


def test_does_not_touch_existing_first_name() -> None:
    users: List[User] = [
        {"first_name": "Alice", "last_name": "Smith",
         "full_name": "Alice Smith"},
        {"first_name": "Bob", "last_name": "Brown",
         "full_name": "Robert Brown"},
    ]
    original: List[User] = copy.deepcopy(users)

    restore_names(users)

    assert users == original  # unchanged


def test_mutates_in_place_same_list_object() -> None:
    users: List[User] = [
        {"first_name": None, "last_name": "Doe", "full_name": "John Doe"},
    ]
    original_id: int = id(users)

    restore_names(users)

    assert id(users) == original_id
    assert users[0]["first_name"] == "John"


@pytest.mark.parametrize(
    "full_name, expected_first",
    [
        ("Anna Karenina", "Anna"),
        ("  Anna   Karenina  ", "Anna"),
        ("Mary Jane Watson", "Mary"),
        ("Jean-Luc Picard", "Jean-Luc"),
        ("Madonna", "Madonna"),
        ("Óscar Isaac Hernández", "Óscar"),
    ],
)
def test_extracts_first_token_from_full_name(
    full_name: str,
    expected_first: str,
) -> None:
    users: List[User] = [
        {"first_name": None, "last_name": "X", "full_name": full_name},
    ]

    restore_names(users)

    assert users[0]["first_name"] == expected_first
    assert users[0]["last_name"] == "X"
    assert users[0]["full_name"] == full_name


def test_mixed_collection_updates_only_needed_entries() -> None:
    users: List[User] = [
        {"first_name": "Kate", "last_name": "A", "full_name": "Kate A"},
        {"first_name": None, "last_name": "B", "full_name": "Leo B"},
        {"last_name": "C", "full_name": "Ivy C"},
        {"first_name": "Mila", "last_name": "D", "full_name": "Mila D"},
    ]

    restore_names(users)

    expected: List[User] = [
        {"first_name": "Kate", "last_name": "A", "full_name": "Kate A"},
        {"first_name": "Leo", "last_name": "B", "full_name": "Leo B"},
        {"first_name": "Ivy", "last_name": "C", "full_name": "Ivy C"},
        {"first_name": "Mila", "last_name": "D", "full_name": "Mila D"},
    ]
    assert users == expected
