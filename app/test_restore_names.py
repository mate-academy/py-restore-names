import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected_users",
                         [([{"first_name": None,
                             "last_name": "Holy",
                             "full_name": "Jack Holy"},
                            {"last_name": "Adams",
                             "full_name": "Mike Adams"},
                            {"first_name": "Dasha",
                             "last_name": "Shostak",
                             "full_name": "Dasha Shostak"}
                            ],
                           [{"first_name": "Jack",
                             "last_name": "Holy",
                             "full_name": "Jack Holy"},
                            {"first_name": "Mike",
                             "last_name": "Adams",
                             "full_name": "Mike Adams"},
                            {"first_name": "Dasha",
                             "last_name": "Shostak",
                             "full_name": "Dasha Shostak"}
                            ])])
def test_restore_names(users: List[dict], expected_users: List[dict]) -> None:
    restore_names(users)
    assert users == expected_users
