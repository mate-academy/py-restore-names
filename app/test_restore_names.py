import pytest

from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": "Jane Smith"},
        {"full_name": "Alice Johnson", "first_name": "Alice"},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Alice"


def test_restore_names_with_no_full_name() -> None:
    users = [
        {"first_name": None},
    ]

    with pytest.raises(KeyError):
        restore_names(users)


def test_restore_names_with_empty_list() -> None:
    users = []

    restore_names(users)

    assert users == []


def test_restore_names_with_partial_names() -> None:
    users = [
        {"full_name": "John"},
        {"full_name": "Jane", "first_name": None},
    ]

    restore_names(users)

    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
