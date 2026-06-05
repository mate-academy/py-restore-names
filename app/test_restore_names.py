import pytest
from app.restore_names import restore_names

def test_first_name_none():
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

def test_no_first_name():
    users = [{"full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

def test_if_first_name_have():
    users = [{"first_name": "Jack", "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"