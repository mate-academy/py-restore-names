from typing import List
from app.restore_names import restore_names


def test_restore_names_fills_missing_first_name() -> None:
    users = [{"full_name": "John Doe", "first_name": None}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_fills_when_key_missing() -> None:
    users = [{"full_name": "Alice Brown"}]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"


def test_restore_names_leaves_existing_first_name_unchanged() -> None:
    users = [{"full_name": "Jane Smith", "first_name": "Jane"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jane"


def test_restore_names_handles_empty_list() -> None:
    users: List[dict] = []
    restore_names(users)
    assert len(users) == 0


def test_restore_names_multiple_users() -> None:
    users = [
        {"full_name": "Bob Johnson", "first_name": None},
        {"full_name": "Eve Davis"},
        {"full_name": "Frank Wilson", "first_name": "Frank"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"
    assert users[1]["first_name"] == "Eve"
    assert users[2]["first_name"] == "Frank"
