import pytest
from typing import List, Dict, Optional

from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
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


def test_restore_names_empty() -> None:
    users: List[Dict[str, Optional[str]]] = []
    restore_names(users)
    assert users == []


def test_restore_names_no_last_name() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Jack",
        },
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "full_name": "Jack",
        },
    ]


if __name__ == "__main__":
    pytest.main()
