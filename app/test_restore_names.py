import pytest
from app.restore_names import restore_names


@pytest.fixture()
def list_of_users1() -> list[dict]:
    user1 = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return user1


def test_restore_names(list_of_users1: list[dict]) -> None:
    users = list_of_users1
    restore_names(users)
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
    ]
