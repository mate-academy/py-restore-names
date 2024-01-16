import pytest
from app.restore_names import restore_names


@pytest.fixture()
def test_users() -> list[dict]:
    yield [
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


def test_restore_names(test_users: list[dict]) -> None:
    restore_names(test_users)
    for user in test_users:
        assert user["first_name"] == user["full_name"].split()[0]
