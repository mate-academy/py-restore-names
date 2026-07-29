import pytest
from app import restore_names


@pytest.fixture
def users() -> list[dict[str, str]]:
    return [
        {"full_name": "John Doe", "first_name": None},
        {"full_name": " Jane Smith", "first_name": None},
        {"full_name": "Alice Johnson "},
        {"full_name": "Charlie  Wilson", "first_name": None},
        {"full_name": "Bob Brown", "first_name": "Bob"},
    ]


@pytest.fixture
def expected_result() -> list[dict[str, str]]:
    return [
        {"full_name": "John Doe", "first_name": "John"},
        {"full_name": " Jane Smith", "first_name": "Jane"},
        {"full_name": "Alice Johnson ", "first_name": "Alice"},
        {"full_name": "Charlie  Wilson", "first_name": "Charlie"},
        {"full_name": "Bob Brown", "first_name": "Bob"},
    ]


def test_restore_names(users: list[dict[str, str]], expected_result: list[dict[str, str]]) -> None:
    restore_names.restore_names(users)
    assert users == expected_result
