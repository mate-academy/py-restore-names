import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> dict:
    yield {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


def test_first_name_is_none(user: dict) -> None:
    user["first_name"] = None
    restore_names([user])
    assert user["first_name"] == "Jack"


def test_first_name_is_not_exist(user: dict) -> None:
    del user["first_name"]
    restore_names([user])
    assert user["first_name"] == "Jack"
