import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users() -> list:
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
            "first_name": "John",
            "last_name": "Brown",
            "full_name": "John Brown",
        },
    ]


def test_restore_names(users: list) -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["full_name"].split()[0]
