import pytest
from app.restore_names import restore_names


example_users = [
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


def test_restore_names_with_missing_first_name() -> None:
    users = example_users.copy()
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        }
    ]
    # Ensure the function does not modify existing first_name
    restore_names(users)
    assert users == [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]


def test_restore_names_with_empty_list() -> None:
    users = []
    # Ensure the function works with an empty list
    restore_names(users)
    assert users == []


if __name__ == "__main__":
    pytest.main()
