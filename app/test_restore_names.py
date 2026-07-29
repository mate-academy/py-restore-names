import pytest
from app.restore_names import restore_names


def test_if_name_restoring(users_list: list) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == "Jack"
    assert users_list[1]["first_name"] == "Mike"


@pytest.fixture
def users_list() -> list:
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
