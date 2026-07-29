import pytest
from app.restore_names import restore_names


@pytest.fixture
def actual_users() -> list[dict]:
    return [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]


def test_restore_names(actual_users: list) -> None:
    restore_names(actual_users)
    expected_users = [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]
    assert actual_users == expected_users
