import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_list() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_with_first_name_is_none(user_list: list) -> None:
    restore_names(user_list)
    assert user_list == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_names_with_first_name_is_not_exist(user_list: list) -> None:
    user_list = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(user_list)
    assert user_list == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
