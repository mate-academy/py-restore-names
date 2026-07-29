import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def failed_db_users() -> List[dict]:
    return [
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


@pytest.fixture()
def fixed_db_users() -> List[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_names(
        failed_db_users: List[dict],
        fixed_db_users: List[dict]
) -> None:

    restore_names(failed_db_users)
    assert failed_db_users == fixed_db_users
