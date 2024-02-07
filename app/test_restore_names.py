from typing import List, Dict, Any
import pytest
from app.restore_names import restore_names
from unittest.mock import patch


@pytest.fixture
def mock_users() -> List[Dict[str, Any]]:
    return [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]


@patch("app.restore_names")
def test_restore_names(mock_restore_names: Any,
                       mock_users: List[Dict[str, Any]]) -> None:
    mock_restore_names.return_value = None

    restore_names(mock_users)

    assert mock_users[0]["first_name"] == "Jack"
    assert mock_users[1]["first_name"] == "Mike"
