import pytest
from app.restore_names import restore_names
from typing import List


@pytest.fixture()
def users() -> list:
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
    return users


def test_restore_names(users: List[dict]) -> None:
    restore_names(users)
    for user in users:
        assert "first_name" in user and user["first_name"] is not None
