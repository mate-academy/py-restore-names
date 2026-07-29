import pytest
from typing import List
from app.restore_names import restore_names


@pytest.fixture
def user_template() -> None:
    user_template = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"}
    ]
    return user_template


def test_cryptocurrency_action(user_template: List[dict]) -> None:
    restore_names(users=user_template)
    assert user_template == [
        {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}
    ]
