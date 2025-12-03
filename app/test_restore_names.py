import pytest
from app.restore_names import restore_names


@pytest.fixture
def dict_user() -> list[dict]:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]


def test_return_restore_names(dict_user: list[dict]) -> None:
    assert restore_names(dict_user) is None


def test_first_name_is_none(dict_user: list[dict]) -> None:
    dict_user[0]["first_name"] = None
    restore_names(dict_user)
    assert dict_user[0]["first_name"] == "Jack"


def test_last_name_is_none(dict_user: list[dict]) -> None:
    del dict_user[0]["first_name"]
    restore_names(dict_user)
    assert dict_user[0]["first_name"] == "Jack"
