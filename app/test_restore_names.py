import pytest
from app.restore_names import restore_names

def restore_names(users: List[dict]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            user["first_name"] = user["full_name"].split()[0]
def test_restore_when_first_name_is_none():
    users = [
        {"first_name": None, "last_name": "Smith", "full_name": "John Smith"},
        {"last_name": "Doe", "full_name": "Jane Doe"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
def test_no_change_when_first_name_present():
    users = [
        {"first_name": "Alice", "last_name": "Wonderland", "full_name": "Alice Wonderland"},
        {"first_name": "Bob", "last_name": "Builder", "full_name": "Bob Builder"},
    ]
    expected = users.copy()
    restore_names(users)
    assert users == expected
def test_restore_with_multiple_users():
    users = [
        {"first_name": None, "last_name": "Black", "full_name": "John Black"},
        {"last_name": "White", "full_name": "Jane White"},
        {"first_name": "Charlie", "last_name": "Brown", "full_name": "Charlie Brown"},
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Charlie"
def test_restore_first_name_not_in_user_dict():
    users = [
