from typing import List

import pytest
from app.restore_names import restore_names

@pytest.fixture
def set_users_for_test() -> list[dict]:
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

def test_restore_names(set_users_for_test: list[dict]) -> None:
    restore_names(set_users_for_test)
    assert set_users_for_test[0]["first_name"] == "Jack"
    assert set_users_for_test[1]["first_name"] == "Mike"


