import pytest
from app.restore_names import restore_names


@pytest.fixture
def users() -> list:
    return [
        {"full_name": "Alice Johnson"},
        {"first_name": None, "full_name": "Bob Smith"},
        {"first_name": "Charlie", "full_name": "Charlie Brown"},
        {"first_name": None, "full_name": "Eve"},
        {"full_name": "Frank"}
    ]


def test_restore_names(users: any) -> None:
    restore_names(users)

    expected = [
        {"first_name": "Alice", "full_name": "Alice Johnson"},
        {"first_name": "Bob", "full_name": "Bob Smith"},
        {"first_name": "Charlie", "full_name": "Charlie Brown"},
        {"first_name": "Eve", "full_name": "Eve"},
        {"first_name": "Frank", "full_name": "Frank"}
    ]

    assert users == expected
