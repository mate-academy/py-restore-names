import pytest
from typing import List

from app.restore_names import restore_names


@pytest.fixture
def sample_data() -> List[dict]:
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
            "first_name": None,
            "last_name": "Brown",
            "full_name": "A.J. Brown",
        },
    ]
    restore_names(users)
    return users


def test_restore_names(sample_data: List[dict]) -> None:
    restore_names(sample_data)

    assert sample_data[0]["first_name"] == "Jack"
    assert sample_data[1]["first_name"] == "Mike"
    assert sample_data[2]["first_name"] == "A.J."
