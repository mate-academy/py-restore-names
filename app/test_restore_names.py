import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_database() -> list[dict]:
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


def test_restore_names(users_database: list[dict]) -> None:
    restore_names(users_database)
    assert users_database[0]["first_name"] == "Jack"
    assert users_database[1]["first_name"] == "Mike"
