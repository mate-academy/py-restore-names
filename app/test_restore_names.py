import pytest
from app.restore_names import restore_names


def test_restore_names_users_with_missing_first_name() -> None:
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


def test_restore_names_users_with_existing_first_name() -> None:
    users = [
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


def test_restore_names_users_without_full_name() -> None:
    users = [
        {
            "first_name": "Mark",
            "last_name": "Brown",
        },
        {
            "first_name": None,
            "last_name": "Johnson",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Mark",
            "last_name": "Brown",
        },
        {
            "first_name": "Mike",
            "last_name": "Johnson",
        },
    ]


if __name__ == "__main__":
    pytest.main()
