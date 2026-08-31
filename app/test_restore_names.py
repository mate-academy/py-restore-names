from typing import List

import pytest

from app import restore_names


@pytest.fixture()
def users() -> List[dict]:
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
        {
            "first_name": "Alice",
            "last_name": "Cooper",
            "full_name": "Alice Cooper",
        },
    ]


def test_restore_names(users: List[dict]) -> None:
    result = restore_names.restore_names(users)

    assert result is None
    assert users == [
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
        {
            "first_name": "Alice",
            "last_name": "Cooper",
            "full_name": "Alice Cooper",
        },
    ]
