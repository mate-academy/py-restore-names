from app.restore_names import restore_names

from typing import List, Dict

import pytest


def create_user(
        first_name: str | None,
        last_name: str,
        full_name: str
) -> Dict[str, str]:
    return {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name
    }


def test_restore_names() -> None:
    users = [
        create_user(None, "Holy", "Jack Holy"),
        create_user(None, "Adams", "Mike Adams"),
        create_user("Alice", "Smith", "Alice Smith"),
        create_user(None, "Doe", "John Doe"),
        create_user("", "White", "White"),
        create_user("Bob", "Brown", "Bob Brown"),
    ]

    restore_names(users)

    expected_names = ["Jack", "Mike", "Alice", "John", "", "Bob"]
    actual_names = [user["first_name"] for user in users]
    assert actual_names == expected_names


def test_restore_only_none_names(monkeypatch: pytest.MonkeyPatch) -> None:
    def restore_only_none_names(users: List[Dict[str, str]]) -> None:
        for user in users:
            if user["first_name"] is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(
        "app.restore_names.restore_names",
        restore_only_none_names
    )

    test_data = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]

    restore_only_none_names(test_data)

    expected_names = ["Jack", "Mike"]
    actual_names = [user["first_name"] for user in test_data]
    assert actual_names == expected_names, \
        "First names should be restored correctly from full names."
