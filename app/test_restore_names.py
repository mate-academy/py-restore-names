import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list[dict]:
    return [
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
    ]


def test_restore_names(users: list[dict]) -> None:
    assert "first_name" not in users[0] or users[0]["first_name"] is None
    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"
    assert "first_name" not in users[1] or users[1]["first_name"] is None
    assert users[1]["last_name"] == "Holy"
    assert users[1]["full_name"] == "Jack Holy"
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
    assert users[0]["last_name"] == "Adams"
    assert users[0]["full_name"] == "Mike Adams"
    assert users[1]["first_name"] == "Jack"
    assert users[1]["last_name"] == "Holy"
    assert users[1]["full_name"] == "Jack Holy"
