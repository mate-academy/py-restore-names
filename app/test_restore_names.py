import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def lost_users_data() -> List[dict]:
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
def full_users_data() -> List[dict]:
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
    lost_users_data: List[dict], full_users_data: List[dict]
) -> None:
    restore_names(lost_users_data)
    assert lost_users_data == full_users_data
