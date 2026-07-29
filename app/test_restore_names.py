import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict]:
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


@pytest.fixture
def expected() -> list[dict]:
    expected = [
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
    return expected


def test_restore_names(
        users: list[dict], expected: list[dict]
) -> None:
    test_users = users
    restore_names(users)
    assert test_users == expected
