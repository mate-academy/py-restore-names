import pytest
from app.restore_names import restore_names


@pytest.fixture
def sample_users() -> list[dict]:
    return [
        {"full_name": "Иван Иванов"},
        {"full_name": "Анна Смирнова", "first_name": None},
        {"full_name": "Петр Петров", "first_name": "Петь"}
    ]


def test_restore_names(sample_users: list[dict]) -> None:
    restore_names(sample_users)
    assert sample_users[0]["first_name"] == "Иван"
    assert sample_users[1]["first_name"] == "Анна"
    assert sample_users[2]["first_name"] == "Петь"
