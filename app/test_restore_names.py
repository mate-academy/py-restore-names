from typing import List, Dict, Any
from app.restore_names import restore_names


def test_restore_names_basic() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Alice"

# ... і так далі для інших тестів
