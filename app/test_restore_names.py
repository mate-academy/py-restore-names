import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user() -> list:
    user = [dict(first_name="Mike", last_name="Adams", full_name="Mike Adams")]
    return user


def test_when_first_name_not_excist(user: list) -> None:
    del user[0]["first_name"]
    restore_names(user)
    assert "first_name" in user[0]


def test_when_first_name_is_none(user: list) -> None:
    user[0]["first_name"] = None
    restore_names(user)
    assert user[0]["first_name"] == "Mike"
