import pytest
from app.restore_names import restore_names


def test_restore_only_missing_names() -> None:
    users = [
        {
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


def test_restore_only_none_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
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


def test_restore_names_with_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
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


def test_restore_names_with_only_first_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
            "first_name": None,
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "full_name": "Jane Doe",
        },
    ]


def test_restore_names_with_no_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Unknown",
            "full_name": "Unknown Person",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Unknown",
            "last_name": "Unknown",
            "full_name": "Unknown Person",
        },
    ]


def test_restore_names_with_multiple_first_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "John Michael Brown",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Brown",
            "full_name": "John Michael Brown",
        },
    ]


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


if __name__ == "__main__":
    pytest.main()
