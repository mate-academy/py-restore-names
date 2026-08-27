from typing import Optional

import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected_first_name",
    [
        pytest.param(
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            "Jack",
            id="first_name_is_none",
        ),
        pytest.param(
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            "Mike",
            id="first_name_is_missing",
        ),
        pytest.param(
            {
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "Jack Smith",
            },
            "John",
            id="first_name_already_set",
        ),
    ],
)
def test_restore_names_sets_expected_first_name(
    user: dict[str, Optional[str]], expected_first_name: str
) -> None:
    users = [user]

    restore_names(users)

    assert users[0]["first_name"] == expected_first_name


def test_restore_names_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    result = restore_names(users)

    assert result is None


def test_restore_names_multiple_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
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
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]
