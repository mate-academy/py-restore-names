import pytest
from app.restore_names import restore_names

users = [
    {
        "last_name": "Doe",
        "full_name": "John Doe",
    },
    {
        "first_name": None,
        "last_name": "Doe",
        "full_name": "John Doe",
    },{
        "last_name": "Doe",
        "full_name": "   John    Doe",
    }
]

def test_restore_names_correct_insert_full_name() -> None:
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[0]["last_name"] == "Doe"
    assert users[0]["full_name"] == "John Doe"


def test_restore_names_first_name_when_none() -> None:
    restore_names(users)
    assert users[1]["first_name"] == "John"
    assert users[1]["last_name"] == "Doe"
    assert users[1]["full_name"] == "John Doe"

def test_restore_names_removes_white_spaces() -> None:
    restore_names(users)
    assert users[2]["first_name"] == "John"
    assert users[2]["last_name"] == "Doe"
    assert users[2]["full_name"] == "John Doe"