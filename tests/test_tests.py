from typing import List
import pytest
from app import restore_names

def test_restore_only_missing_names(monkeypatch):
    def restore_only_missing_names(users: List[dict]) -> None:
        for user in users:
            if "first_name" not in user:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(restore_names, "restore_names", restore_only_missing_names)

    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names.restore_names(users)
    assert users == expected, "Function should restore missing first_name"

def test_restore_only_none_names(monkeypatch):
    def restore_only_none_names(users: List[dict]) -> None:
        for user in users:
            if user.get("first_name") is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(restore_names, "restore_names", restore_only_none_names)

    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    expected = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_names.restore_names(users)
    assert users == expected, "Function should restore first_name when it is None"
