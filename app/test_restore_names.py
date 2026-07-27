import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list:
    return [
        {"full_name": "John Doe"},
        {"full_name": "Jane Smith"},
        {"full_name": "Alice Johnson", "first_name": None}
    ]


def test_restore_names(users: list) -> None:
    restore_names(users)
    assert users[0]["first_name"] == "John"
    assert users[1]["first_name"] == "Jane"
    assert users[2]["first_name"] == "Alice"
