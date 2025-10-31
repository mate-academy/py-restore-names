from typing import Generator

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def mock_users() -> Generator:
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
        {
            "first_name": "Jim",
            "last_name": "Blue",
            "full_name": "Jim Blue",
        },
    ]
    yield users


def test_restore_names(mock_users: list) -> None:
    restore_names(mock_users)

    for user in mock_users:
        assert user["first_name"] == user["full_name"].split()[0]
