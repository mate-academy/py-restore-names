import pytest
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": None, "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Chris", "last_name": "Evans"},  # No full_name provided
        {"first_name": None, "last_name": "Lee",
         "full_name": ""},  # Empty full_name
    ]

    restore_names(users)

    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams",
         "full_name": "Mike Adams"},
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Chris", "last_name": "Evans"},
        {"first_name": None, "last_name": "Lee", "full_name": ""},
    ]

    assert users == expected


def test_restore_names_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restore_names_no_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Brown"}  # No full_name field
    ]
    restore_names(users)
    assert users == [{"first_name": None, "last_name": "Brown"}]


if __name__ == "__main__":
    pytest.main()
