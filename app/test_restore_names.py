import pytest
from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
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


def test_restore_names_without_first_name() -> None:
    users = [
        {
            "last_name": "Smith",
            "full_name": "John Smith",
        },
        {
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


def test_no_change_if_first_name_exists() -> None:
    users = [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
        {
            "first_name": "Bob",
            "last_name": "Builder",
            "full_name": "Bob Builder",
        },
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "full_name": "Alice Wonderland",
        },
        {
            "first_name": "Bob",
            "last_name": "Builder",
            "full_name": "Bob Builder",
        },
    ]


if __name__ == "__main__":
    pytest.main()
