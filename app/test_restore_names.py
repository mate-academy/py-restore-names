from typing import List, Dict
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        ),
    ],
)
def test_restore_names_basic(
    input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        ([], []),
    ],
)
def test_restore_names_empty_list(
    input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "Johnny Doe"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "Johnny Doe"
                }
            ],
        ),

    ]
)
def test_restore_names_first_name_present(
    input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [{
                "first_name": None,
                "last_name": "Doe",
                "full_name": "Mary Jane Doe"
            }
            ],
            [{
                "first_name": "Mary",
                "last_name": "Doe",
                "full_name": "Mary Jane Doe"
            }],
        ),
        (
            [{
                "last_name": "Brown",
                "full_name": "Charlie Brown"
            }],
            [{
                "first_name": "Charlie",
                "last_name": "Brown",
                "full_name": "Charlie Brown"
            }],
        ),
    ],
)
def test_restore_names_various_missing_first_names(
    input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "White",
                    "full_name": "Alice White"
                },
                {
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
            ],
            [
                {
                    "first_name": "Alice",
                    "last_name": "White",
                    "full_name": "Alice White"
                },
                {
                    "first_name": "Bob",
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
            ],
        ),
    ],
)
def test_restore_names_mixed_none_and_missing(
    input_users: List[Dict[str, str]], expected_users: List[Dict[str, str]]
) -> None:
    restore_names(input_users)
    assert input_users == expected_users
