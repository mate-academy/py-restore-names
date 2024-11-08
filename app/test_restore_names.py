import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> dict:
    return {"last_name": "Smith", "full_name": "Bob Smith"}


def test_restore_names_with_none(user_template: dict) -> None:
    user_template["first_name"] = None
    restore_names([user_template])
    assert user_template["first_name"] == user_template["full_name"].split()[0]


def test_restore_names_with_empty(user_template: dict) -> None:
    restore_names([user_template])
    assert user_template["first_name"] == user_template["full_name"].split()[0]
