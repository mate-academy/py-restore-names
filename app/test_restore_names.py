from typing import List, Dict
import pytest
from app.restore_names import restore_names


def test_restore_names_with_monkeypatch(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_restore_names(users: List[Dict[str, str]]) -> None:
        for user in users:
            if "first_name" not in user or user["first_name"] is None:
                user["first_name"] = user["full_name"].split()[0]

    monkeypatch.setattr("app.restore_names.restore_names", mock_restore_names)

    input_data: List[Dict[str, str]] = [
        {"first_name": None,
         "last_name": "Doe",
         "full_name": "John Doe"},
        {"last_name": "Smith",
         "full_name": "Jane Smith"},
        {"first_name": "Anna",
         "last_name": "Taylor",
         "full_name": "Anna Taylor"}
    ]
    expected_data: List[Dict[str, str]] = [
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
        {"first_name": "Jane",
         "last_name": "Smith",
         "full_name": "Jane Smith"},
        {"first_name": "Anna",
         "last_name": "Taylor",
         "full_name": "Anna Taylor"}
    ]

    restore_names(input_data)

    assert input_data == expected_data
