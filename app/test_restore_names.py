# app/test_restore_names.py
from app.restore_names import restore_names


def test_restore_names_with_missing_first_name() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
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


def test_restore_names_does_not_change_valid_entries() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Lee", "full_name": "Anna Lee"},
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected


def test_restore_names_with_multiple_missing_first_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "John Brown",
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: list[dict[str, str | None]] = []
    restore_names(users)
    assert users == []


def test_restore_names_partial_full_name() -> None:
    users = [
        {"first_name": None, "last_name": "Stone", "full_name": "David"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "David"
