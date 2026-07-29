from typing import Any
from app.restore_names import restore_names


def test_should_do_nothing_if_first_name_is_already_present() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_should_restore_name_when_first_name_is_none_or_missing() -> None:
    users: list[dict[str, Any]] = [
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


def test_should_handle_an_empty_list_gracefully() -> None:
    users: list[dict[str, Any]] = []

    restore_names(users)

    assert users == []


def test_should_handle_mixed_scenarios_correctly() -> None:
    users: list[dict[str, Any]] = [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        },
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Sarah",
            "last_name": "Connor",
            "full_name": "Sarah Connor",
        },
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
