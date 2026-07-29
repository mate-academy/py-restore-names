import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture
def users_semple() -> List[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        },
    ]


def test_restore_names_with_sample_users(users_semple: List[dict]) -> None:
    restore_names(users_semple)

    assert users_semple[0]["first_name"] == "Jack"
    assert users_semple[1]["first_name"] == "Mike"
    assert users_semple[2]["first_name"] == "Anna"


def test_empty_input() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_missing_first_name() -> None:
    users = [{"last_name": "Doe"}]
    with pytest.raises(KeyError):
        restore_names(users)
