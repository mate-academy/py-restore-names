import pytest
from app.restore_names import restore_names


@pytest.fixture()
def test_users() -> list:
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


def test_restore_names(test_users: list) -> None:
    restore_names(test_users)
    assert test_users[0]["first_name"] == "Jack"
