import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture()
def data_base() -> List[dict]:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Jack Adams",
        },
    ]

    return users


def test_restore_names(data_base: List[dict]) -> None:
    restore_names(data_base)

    for user in data_base:
        assert user["first_name"] == "Jack"


print(type(data_base))
