import pytest
from app.restore_names import restore_names


def test_is_first_name_in_user_and_none() -> None:
    users = [
        {"last_name": "Lysanets", "full_name": "Oleksandr Lysanets"},
        {"first_name": None, "last_name": "Dub", "full_name": "Ivan Dub"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Oleksandr"
    assert users[1]["first_name"] == "Ivan"
