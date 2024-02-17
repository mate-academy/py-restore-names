import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user() -> dict:
    return {
        "first_name": "Tony",
        "last_name": "Stark",
        "full_name": "Tony Stark",
    }


def test_restore_none_name(user: dict) -> None:
    user["first_name"] = None

    restore_names([user])

    assert user["first_name"] == "Tony"


def test_restore_missing_name(user: dict) -> None:
    del user["first_name"]

    restore_names([user])

    assert user["first_name"] == "Tony"
