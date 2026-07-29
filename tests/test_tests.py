from typing import List, Dict, Any
import pytest
from app import restore_names as rn_module


def test_restore_only_missing_names(
    monkeypatch: "pytest.MonkeyPatch",
) -> None:
    def restore_only_missing(users: List[Dict[str, Any]]) -> None:
        for user in users:
            if "first_name" not in user or user["first_name"] is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(
        rn_module,
        "restore_names",
        restore_only_missing
    )

    users: List[Dict[str, Any]] = [
        {"last_name": "Doe", "full_name": "John Doe"},
        {"first_name": "Alice", "last_name": "Adams",
         "full_name": "Alice Adams"},
    ]
    rn_module.restore_names(users)
    first_names = [user["first_name"] for user in users]
    assert first_names == ["John", "Alice"]


def test_restore_only_none_names(
    monkeypatch: "pytest.MonkeyPatch",
) -> None:
    def restore_only_none(users: List[Dict[str, Any]]) -> None:
        for user in users:
            if user.get("first_name") is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr(
        rn_module,
        "restore_names",
        restore_only_none
    )

    users: List[Dict[str, Any]] = [
        {"first_name": None, "last_name": "Doe",
         "full_name": "Mary Jane Doe"}
    ]
    rn_module.restore_names(users)
    assert users[0]["first_name"] == "Mary"
