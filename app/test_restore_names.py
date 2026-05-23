import pytest
from app.restore_names import restore_names

def test_restore_names_with_none():
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
