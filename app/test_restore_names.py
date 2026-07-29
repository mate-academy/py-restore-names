import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_dict() -> list:
    return [{"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"}]


def test_restore_names_with_none(user_dict: list) -> None:
    user_dict[0]["first_name"] = None
    restore_names(user_dict)
    assert user_dict[0] == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


def test_restore_names_with_no_key(user_dict: list) -> None:
    del user_dict[0]["first_name"]
    restore_names(user_dict)
    assert user_dict[0] == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }


def test_restore_names_do_nothing(user_dict: list) -> None:
    restore_names(user_dict)
    assert user_dict[0] == {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }
