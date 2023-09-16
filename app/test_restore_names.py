import pytest
from app.restore_names import restore_names


def test_missing_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Powell",
            "full_name": "John Powell"
        },
        {
            "first_name": None,
            "last_name": "Churchill",
            "full_name": "Winston Churchill"
        }
    ]
    restore_names(users)
    expected_results = [
        {
            "first_name": "John",
            "last_name": "Powell",
            "full_name": "John Powell"
        },
        {
            "first_name": "Winston",
            "last_name": "Churchill",
            "full_name": "Winston Churchill"
        }
    ]
    assert users == expected_results


def test_restore_names_with_users_missing_and_some_with_first_name():
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
        {
            "first_name": None,
            "last_name": "Johnson",
            "full_name": "Emily Johnson",
        },
    ]

    restore_names(users)

    expected_results = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "full_name": "Jane Smith",
        },
        {
            "first_name": "Emily",
            "last_name": "Johnson",
            "full_name": "Emily Johnson",
        },
    ]
    assert users == expected_results
